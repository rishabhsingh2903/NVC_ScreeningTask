import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

const BarChart = ({ data }) => {
  const svgRef = useRef();

  useEffect(() => {
    if (!data || data.length === 0) {
      return;
    }

    const companyTotal = d3.rollup(
      data,
      (y) => d3.sum(y, (x) => x.price),
      (x) => x.company
    );

    const chartData = Array.from(companyTotal, ([company, total]) => ({
      company,
      total,
    }));
    // console.log(chartData);
    const width = 500;
    const height = 300;
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };

    const svg = d3
      .select(svgRef.current)
      .attr("width", width)
      .attr("height", height);

    svg.selectAll("*").remove();

    const x = d3
      .scaleBand()
      .domain(chartData.map((d) => d.company))
      .range([margin.left, width - margin.right])
      .padding(0.1);

    const y = d3
      .scaleLinear()
      .domain([0, d3.max(chartData, (d) => d.total)])
      .nice()
      .range([height - margin.bottom, margin.top]);

    svg
      .selectAll("rect")
      .data(chartData)
      .join("rect")
      .attr("x", (d) => x(d.company))
      .attr("y", (d) => y(d.total))
      .attr("height", (d) => y(0) - y(d.total))
      .attr("width", x.bandwidth())
      .attr("fill", "steelblue");

    svg
      .append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x));

    svg
      .append("g")
      .attr("transform", `translate(${margin.left}, 0)`)
      .call(d3.axisLeft(y));
  }, [data]);
  return (
    <div>
      <h3 className="font-semibold mb-2">Total Sales by Company</h3>
      <svg ref={svgRef}></svg>
    </div>
  );
};
export default BarChart;
