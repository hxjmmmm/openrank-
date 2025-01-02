<template>
  <div id="chart" style="width: 100%; height:8rem">
 
  </div>
  
</template>
<script>
import * as  echarts from "echarts";
export default {
props: {
  nodes2: Array,
  links2: Array
  },
data() {
  return {
    categories:[
        {
            "name": "repo"
        },
        {
            "name": "issue"
        },
        {
            "name": "pull"
        },
        {
            "name": "user"
        },
    ],
    s:[],
    a:[],
    
};
},
computed: {
  
  },
  mounted() {
    // 当组件挂载后，打印 receivedData prop
    this.$nextTick(() => {
      this.initChart();
    });
 
},
methods: {
  initChart() {
    //初始化echarts
    let myChart = echarts.init(document.getElementById('chart'))
 
    myChart.resize();  //自适应大小
    myChart.setOption(this.setOption());
    myChart.hideLoading();
  },
  //初始化echarts
  setOption() {
    let option = {
      tooltip: {},
    legend: [
      {
        data:this.categories.map(function (a) {
          return a.name;
        })
      }
    ],
    series: [
      {
        name: 'open',
        type: 'graph',
        layout: "force", // 使用力导向布局
            force: {
              repulsion: 500, // 增加节点之间的排斥力
              edgeLength: 200, // 边的长度，调节连线的紧密度
              gravity: 0.1, // 设置重力感应，让节点向图中心聚集
    },
        data: this.s,
        links: this.a,
        categories:this.categories,
        roam: true,
        label: {
          show: true,
          position: 'right',
          formatter: '{b}'
        },
        labelLayout: {
          hideOverlap: true
        },
        scaleLimit: {
          min: 0.4,
          max: 2
        },
        lineStyle: {
          color: 'source',
          curveness: 0.3
        }
      }
    ]
    };
    return option;
  },

},
watch: {
  // 监听单个 prop
  nodes2: {
    handler(newVal) {
      if (newVal && newVal.length) {
        this.s = newVal;
          this.initChart(); 
      }
    },
    deep: true,
    immediate: true
  },
  // 监听另一个 prop
  links2: {
    handler(newVal) {
      if (newVal && newVal.length) {
        this.a = newVal; 
          this.initChart(); 
      }
    },
    deep: true,
    immediate: true
  }
  }
};
</script>

<style lang="scss" scoped>
</style>
