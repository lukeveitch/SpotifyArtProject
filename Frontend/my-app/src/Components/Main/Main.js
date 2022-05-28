import React from "react";
import s from "./Main.styles";
import Sketch from "../Sketch/Sketch";
import {ReactP5Wrapper} from "react-p5-wrapper";

export const Main = () => {
  return (
      <>
        <s.Description>
          This is a placeholder for a brief description of the concept
        </s.Description>
        <div className="sketch-wrapper">
          <ReactP5Wrapper sketch={Sketch}/>
        </div>
      </>
  );
};
