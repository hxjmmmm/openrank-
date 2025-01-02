<template>
    <div id="chart" style="width: 100%; height: 400px;"></div>
    
      
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
                "name": "pojo"
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
        a:[]
        
    };
    },
    computed: {
      
      },
      mounted() {
        // 当组件挂载后，打印 receivedData prop
    
        this.initChart();
    
     
    },
    methods: {
      initChart() {
        let chartDom = document.getElementById('chart');
      if (chartDom) {
        let myChart = echarts.init(chartDom);
        myChart.resize();  // 确保图表自适应大小
        myChart.setOption(this.setOption());
        myChart.hideLoading();
      }
        
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
        animationDuration: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
          {
            name: 'Les Miserables',
            type: 'graph',
            layout: 'circular',
            force: {
      repulsion: 200,  // 吸引力或排斥力
      edgeLength: 500  // 边的长度
    },
        data: this.s.map((node) => ({
              name: node.name,       // 节点名字
              x: node.x,             // x坐标
              y: node.y,             // y坐标
              category: node.category,  // 类别
              symbolSize: node.symbolSize  // 根据 symbolSize 设置节点大小
            })),
            links: this.a.map(link => ({
              source: link.source,  // 连接的起始节点
              target: link.target   // 连接的目标节点
            })),
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
      color: 'source',  // 使用源节点的颜色
      width: 2,         // 边宽度
      curveness: 0.3    // 边的弯曲程度
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
          this.s = newVal; // 更新数据
          this.$nextTick(() => {
            this.initChart(); // 确保 DOM 渲染后再初始化图表
          });
        },
        deep: true, // 深度监听，用于监听对象内部值的变化
        immediate: true // 组件实例化后立即以当前值执行回调
      },
      // 监听另一个 prop
      links2: {
        handler(newVal) {
          this.a = newVal; // 更新数据
          this.$nextTick(() => {
            this.initChart(); // 确保 DOM 渲染后再初始化图表
          });
        },
        deep: true,
        immediate: true
      }
    },
    
    };
    </script>
    
    <style lang="scss" scoped>
    </style>
    