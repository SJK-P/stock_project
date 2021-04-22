"use strict";

var ctx = document.getElementById("myChart");
// var myChart = new Chart(ctx, {
//     type: "bar",
//     data: {
//         labels: labels,
//         datasets: [
//             {
//                 label: "# of Votes",
//                 data: [12, 19, 3, 5, 2, 3],
//                 backgroundColor: [
//                     "rgba(255, 99, 132, 0.2)",
//                     "rgba(54, 162, 235, 0.2)",
//                     "rgba(255, 206, 86, 0.2)",
//                     "rgba(75, 192, 192, 0.2)",
//                     "rgba(153, 102, 255, 0.2)",
//                     "rgba(255, 159, 64, 0.2)",
//                 ],
//                 borderColor: [
//                     "rgba(255, 99, 132, 1)",
//                     "rgba(54, 162, 235, 1)",
//                     "rgba(255, 206, 86, 1)",
//                     "rgba(75, 192, 192, 1)",
//                     "rgba(153, 102, 255, 1)",
//                     "rgba(255, 159, 64, 1)",
//                 ],
//                 borderWidth: 1,
//             },
//         ],
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true,
//             },
//         },
//     },
// });

const data = {
    labels: labels,
    datasets: [
        {
            type: "bar",
            label: "Volume",
            order: 2,
            backgroundColor: "rgba(179, 198, 255, 1)",
            borderColor: "rgba(179, 198, 255, 1)",
            data: volumes,
            yAxisID: "right-y-axis",
        },

        {
            type: "line",
            label: "Price",
            order: 1,
            backgroundColor: "rgb(0, 57, 230)",
            borderColor: "rgb(0, 57, 230)",
            data: prices,
            yAxisID: "left-y-axis",
        },
    ],
};

const config = {
    type: "scatter",
    data: data,
    options: {
        plugins: {
            datalabels: {
                display: true,
            },
            //     title: {
            //         text: "Chart.js Combo Time Scale",
            //         display: false,
            //     },
        },
        scales: {
            "right-y-axis": {
                type: "linear",
                position: "right",
            },
            "left-y-axis": {
                type: "linear",
                position: "left",
            },
        },
    },
};

var myChart = new Chart(ctx, config);
