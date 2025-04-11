import React, { useState, useEffect } from "react";
import axios from "axios";
import BarChart from "./BarChart";

const TaskAnalytics = ({ taskId }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`http://localhost:8000/tasks/${taskId}/data`)
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [taskId]);

  return (
    <div className="p-4 space-y-6">
      <h2 className="text-2xl font-bold">Task #{taskId} Analytics</h2>
      <BarChart data={data} />
    </div>
  );
};
export default TaskAnalytics;
