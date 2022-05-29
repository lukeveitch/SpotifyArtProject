function Sketch(p) {
  let dimension = 800;
  // let backgroundColor = 0;

  p.setup = function () {
    p.createCanvas(dimension, dimension);
    // p.background(backgroundColor);
    p.blendMode(p.BURN)
    p.frameRate(4);

    let c1 = "#ffb2b2"
    let c2 = "#9affe6"
    let c3 = "#a223ff"
    const coloursArray = [c1, c2, c3];

    //backgroundSquare
    p.push();
    p.noFill();
    p.stroke('white')
    p.strokeWeight(4);
    p.square(0, 0, dimension);
    p.pop();

    p.push();
    p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
    p.circle(Math.floor(Math.random() * dimension), Math.floor(Math.random() * dimension), Math.floor(Math.random() * dimension/ 4))
    p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
    p.circle(Math.floor(Math.random() * dimension), Math.floor(Math.random() * dimension), Math.floor(Math.random() * dimension/ 3))
    p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
    p.circle(Math.floor(Math.random() * dimension), Math.floor(Math.random() * dimension), Math.floor(Math.random() * dimension / 2))
    p.pop();

    //squares generation
    // p.push();
    // let i = 0;
    // while (i <= 11) {
    //   let j = 0;
    //   while (j <= 11) {
    //         let posX = i * 80;
    //         let posY = j * 80;
    //         let dist = p.random(35);
    //
    //         let squareSize = p.random(50);
    //         let squareSize2 = p.random(50);
    //         let squareSize3 = p.random(50);
    //
    //         p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
    //         p.rect(posX, posY, squareSize, squareSize2);
    //         p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
    //         p.rect(posX + dist, posY + dist, squareSize3, squareSize);
    //         p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
    //         p.rect(posX + dist * 2, posY + dist * 2, squareSize3, squareSize2);
    //     j += 1;
    //   }
    //   i += 1;
    // }
    // p.pop();





    p.draw = () => {

      let i = Math.floor(Math.random() * 11);
      let j = Math.floor(Math.random() * 11);

      let posX = i * 80;
      let posY = j * 80;
      let dist = p.random(30);

      let squareSize = p.random(50);
      let squareSize2 = p.random(50);
      let squareSize3 = p.random(50);

      p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
      p.rect(posX, posY, squareSize, squareSize2);
      p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
      p.rect(posX - dist, posY + dist, squareSize3, squareSize);
      p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
      p.rect(posX + dist * 2, posY + dist * 2, squareSize3, squareSize2);

    };
  }
}

export default Sketch;
