function Sketch(p) {
  p.setup = function () {
    p.createCanvas(1000, 1000);
    p.background(0);
    p.blendMode(p.ADD)

    let c1 = "#ffb2b2"
    let c2 = "#9affe6"
    let c3 = "#a223ff"
    const coloursArray = [c1, c2, c3];

    let i = 0;
    while (i <= 11) {
      let j = 0;
      while (j <= 11) {
            let posX = i * 80;
            let posY = j * 80;
            let dist = p.random(35);

            let squareSize = p.random(50);
            let squareSize2 = p.random(50);
            let squareSize3 = p.random(50);

            p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
            p.rect(posX, posY, squareSize, squareSize2);
            p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
            p.rect(posX + dist, posY + dist, squareSize3, squareSize);
            p.fill(coloursArray[Math.floor(Math.random() * coloursArray.length)]);
            p.rect(posX + dist * 2, posY + dist * 2, squareSize3, squareSize2);
        j += 1;
      }
      i += 1;
    }

    console.log("we are done");

    p.draw = () => {

    };
  }
}

export default Sketch;
