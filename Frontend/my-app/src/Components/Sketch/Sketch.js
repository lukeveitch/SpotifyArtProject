import React, {useEffect} from "react";
import * as p5 from "p5";
import s from "./Sketch.styles";

const Sketch1 = p5 => {
  p5.setup = () => {
    let canvas = p5.createCanvas(p5.windowWidth, p5.windowHeight);
    canvas.parent('container')
    p5.background(0);
    p5.blendMode(p5.ADD);

    let c1 = "#ffb2b2"
    let c2 = "#9affe6"
    let c3 = "#a223ff"
    const coloursArray = [c1, c2, c3];

    let i = 0;
    while (i < 10) {
      i += 1;

      let j = 0;
      while (j < 10) {
        j += 1;

        let posX = i * 80;
        let posY = j * 80;
        let dist = p5.random(35);

        let squareSize = p5.random(50);
        let squareSize2 = p5.random(50);
        let squareSize3 = p5.random(50);

        p5.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
        p5.rect(posX, posY, squareSize, squareSize2);
        p5.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
        p5.rect(posX + dist, posY + dist, squareSize3, squareSize);
        p5.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
        p5.rect(posX + dist * 2, posY + dist * 2, squareSize3, squareSize2);

      }
    }
    console.log("we are done");

  };

  p5.draw = () => {
    // p5.rect(p5.mouseX, p5.mouseY, 50, 50);
    // p5.ellipse(p5.width / 2, p5.height / 2, radius, radius);
    // radius++;
  };
};

const Sketch = () => {

  useEffect(() => {
    new p5(Sketch1);
  }, []);

  return (
      <div id="container" style={{margin: "auto",
        width: "50%",
        border: "5px solid red"}}>
      </div>

  );
};

export default Sketch;
