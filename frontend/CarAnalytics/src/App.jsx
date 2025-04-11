import React from "react";
import TaskAnalytics from "./components/TaskAnalytics";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="container mx-auto">
        <div className="grid grid-cols-12">
          <div className=" bg-red-500 col-span-12 lg:col-span-7">
            <TaskAnalytics taskId={1} />
          </div>

          <div className=" bg-green-500 col-span-12 lg:col-span-5">
            
          </div>
        </div>
        <div className=" bg-blue-500 grid grid-cols-12">
          <h1>Hello</h1>
        </div>
      </div>
    </div>
  );
}

export default App;
