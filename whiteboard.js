import React, { useRef, useState } from "react";
import axios from 'axios';

const Whiteboard = () => {
  const canvasRef = useRef(null);
  const [color, setColor] = useState('black');
  const [brushSize, setBrushSize] = useState(5);
  const [isDrawing, setIsDrawing] = useState(false);

  const startDrawing = (e) => {
    const ctx = canvasRef.current.getContext("2d");
    ctx.lineWidth = brushSize;
    ctx.strokeStyle = color;
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    setIsDrawing(true);
    draw(e);
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const ctx = canvasRef.current.getContext("2d");
    ctx.lineTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
    ctx.stroke();
  };

  const endDrawing = () => {
    setIsDrawing(false);
    canvasRef.current.getContext("2d").beginPath();
  };

  const clearCanvas = () => {
    const ctx = canvasRef.current.getContext("2d");
    ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
  };

  const takeScreenshot = async () => {
    const canvas = canvasRef.current;
    const image = canvas.toDataURL("image/png");

    // Send the screenshot to the backend for processing
    try {
      const response = await axios.post("/process_image", { image });
      alert(response.data.text); // Display the AI response
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <h1>Whiteboard App</h1>
      <canvas
        ref={canvasRef}
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={endDrawing}
        width={1000}
        height={500}
        style={{ border: "1px solid black" }}
      />
      <br />
      <button onClick={clearCanvas}>Clear</button>
      <button onClick={() => setColor("white")}>Eraser</button>
      <button onClick={() => setColor("black")}>Marker</button>
      <button onClick={takeScreenshot}>Process</button>
      <button onClick={() => setBrushSize(brushSize + 2)}>Increase Brush</button>
      <button onClick={() => setBrushSize(brushSize - 2)}>Decrease Brush</button>
    </div>
  );
};

export default Whiteboard;
