<template>
  <div
    ref="currentConfirmedComoareBarChart"
    style="width: 100%; height: 100%"
  ></div>
</template>
<script>
import * as echarts from "echarts";
let chart = null;
export default {
  props: {
    title: String,
    issueTime: Array,
    issuesCreated: Array,
    issuesClosed: Array,
  },
  data() {
    return {
      dateList: [],
      curedCountList: [],
      confirmedCountList: [],
    };
  },
  mounted() {
    // 当组件挂载后，打印 receivedData prop
    this.$nextTick(() => {
      this.initChart();
    });
  },
  methods: {
    initChart() {
      if (null != chart && undefined != chart) {
        chart.dispose();
      }
      chart = this.$echarts.init(this.$refs.currentConfirmedComoareBarChart);
      this.setOptions();
    },
    setOptions() {
      let option = {
        title: {
          text: this.title,
          x: "center",
          y: 0,
          textStyle: {
            color: "#B4B4B4",
            fontSize: 14,
            fontWeight: "normal",
          },
        },
        // backgroundColor: '#191E40',
        tooltip: {
          trigger: "axis",
          backgroundColor: "rgba(255,255,255,0.9)",
          axisPointer: {
            type: "shadow",
            label: {
              show: true,
              backgroundColor: "#7B7DDC",
            },
          },
        },
        legend: {
          data: ["新增", "关闭"],
          textStyle: {
            color: "#B4B4B4",
          },
          top: "5%",
        },
        grid: {
          x: "12%",
          width: "82%",
          y: "12%",
        },
        xAxis: {
          data: this.dateList,
          axisLine: {
            lineStyle: {
              color: "#B4B4B4",
            },
          },
          axisTick: {
            show: false,
          },
        },
        yAxis: [
          {
            splitLine: { show: false },
            axisLine: {
              lineStyle: {
                color: "#B4B4B4",
              },
            },
            axisLabel: {
              formatter: "{value} ",
            },
          },
          {
            splitLine: { show: false },
            axisLine: {
              lineStyle: {
                color: "#B4B4B4",
              },
            },
            axisLabel: {
              formatter: "{value} ",
            },
          },
        ],
        series: [
          {
            name: "新增",
            type: "bar",
            barWidth: 10,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "#956FD4" },
                  { offset: 1, color: "#3EACE5" },
                ]),
              },
            },
            data: this.curedCountList,
          },
          {
            name: "关闭",
            type: "bar",
            barGap: "-100%",
            barWidth: 10,
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "rgba(119,60,243,0.7)" },
                  { offset: 0.3, color: "rgba(119,60,243,0.5)" },
                  { offset: 1, color: "rgba(119,60,243,0)" },
                ]),
              },
            },
            z: -12,
            data: this.confirmedCountList,
          },
        ],
      };
      chart.setOption(option);
    },
  },
  watch: {
    // 监听单个 prop
    issueTime: {
      handler(newVal) {
        if (newVal && newVal.length) {
          this.dateList = newVal;
          this.initChart();
        }
      },
      deep: true,
      immediate: true,
    },
    // 监听另一个 prop
    issuesCreated: {
      handler(newVal) {
        if (newVal && newVal.length) {
          this.curedCountList = newVal;
          this.initChart();
        }
      },
      deep: true,
      immediate: true,
    },
    issuesClosed: {
      handler(newVal) {
        if (newVal && newVal.length) {
          this.confirmedCountList = newVal;
          this.initChart();
        }
      },
      deep: true,
      immediate: true,
    }, 
  },
};
</script>