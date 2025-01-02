<template>
  <div ref="basicProportionChart" style="width: 100%; height: 100%"></div>
</template>

<script>
let chart = null;

export default {
  props: {
    languageProportions: Array,
  },
  data() {
    return {
      // 存储随机生成的语言占比数据
      sa:[],
      //新增     1.1 
      
      
    };
  },
  methods: {
    initChart() {
      if (null != chart && undefined != chart) {
        chart.dispose();
      }
      chart = this.$echarts.init(this.$refs.basicProportionChart);
      this.setOptions();
    },
    setOptions() {
      let list = this.sa.map((item, index) => ({
        name: item.language,
        value: item.value,
      }));
      let titleList = [], seriesList = [];
      list.forEach((item, index) => {
        titleList.push({
          text: item.name,
          top: '75%',
          left: index * 30 + 12 + '%',
          textStyle: {
            fontWeight: 'normal',
            color: '#BCBCBF',
            fontSize: '12',
          },
        });
        seriesList.push({
          name: item.name,
          type: 'pie',
          clockWise: true,
          radius: ['50%', '66%'],
          itemStyle: {
            normal: {
              label: {
                show: false,
              },
              labelLine: {
                show: false,
              },
            },
          },
          hoverAnimation: false,
          center: [index * 30 + 20 + '%', '35%'],
          data: [
            {
              value: item.value,
              name: item.name,
              label: {
                normal: {
                  formatter: function (params) {
                    return params.value + '%';
                  },
                  position: 'center',
                  show: true,
                  textStyle: {
                    fontSize: '14',
                    fontWeight: 'bold',
                    color: '#FFF',
                  },
                },
              },
              itemStyle: {
                normal: {
                  color: {
                    colorStops: [
                      { offset: 0, color: '#D32E58' },
                      { offset: 1, color: '#F99266' },
                    ],
                  },
                  label: {},
                  labelLine: { show: false },
                },
              },
            },
            { name: 'Others', value: 100 - item.value },
          ],
        });
      });
      let option = {
        title: titleList,
        color: ['rgba(7, 158, 254, .9)'],
        series: seriesList,
      };
      chart.setOption(option);
    },


  },
  watch: {
  // 监听单个 prop
  languageProportions: {
    handler(newVal) {
      if (newVal && newVal.length) {
        this.sa = newVal;
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
  },
  mounted() {
    this.initChart();

    
  },
};
</script>


<!-- <template>
  <div ref="basicProportionChart" style="width: 100%; height: 100%"></div>
</template>
<script>
let chart = null
const calculateProportion = (value, total) => {
  return ((value / total) * 100).toFixed(0)
}
export default {
  props: {
    data: Object
  },
  methods: {
    initChart () {
      if (null != chart && undefined != chart) {
        chart.dispose()
      }
      chart = this.$echarts.init(this.$refs.basicProportionChart)
      this.setOptions()
    },
    setOptions() {
      let list = [
        {
          name: 'java',
          value: calculateProportion(this.data.currentConfirmedCount, this.data.confirmedCount)
        },
        {
          name: 'c++',
          value: calculateProportion(this.data.importedCount, this.data.confirmedCount)
        },
        {
          name: '其他',
          value: calculateProportion(this.data.curedCount, this.data.confirmedCount)
        }
      ]
      let titleList = [], seriesList = []
      list.forEach((item, index) => {
        titleList.push({
          text: item.name,
          top: '75%',
          left: index * 30 + 12 + '%',
          textStyle: {
            fontWeight: 'normal',
            color: '#BCBCBF',
            fontSize: '12'
          }
        })
        // 
        seriesList.push(
          {
            name: item.name,
            type: 'pie',
            clockWise: true,
            radius: ['50%', '66%'],
            itemStyle: {
              normal: {
                label: {
                  show: false
                },
                labelLine: {
                  show: false
                }
              }
            },
            hoverAnimation: false,
            center: [index * 30 + 20 + '%', '35%'],
            data: [
              {
                value: item.value,
                name: item.name,
                label: {
                  normal: {
                    formatter: function (params) {
                      return params.value + '%';
                    },
                    position: 'center',
                    show: true,
                    textStyle: {
                      fontSize: '14',
                      fontWeight: 'bold',
                      color: '#FFF'
                    }
                  }
                },
                itemStyle: {
                  normal: {
                    color: { // 完成的圆环的颜色
                      colorStops: [{
                        offset: 0,
                        color: '#D32E58' // 0% 处的颜色
                      }, {
                        offset: 1,
                        color: '#F99266' // 100% 处的颜色
                      }]
                    },
                    label: {
                      // show: false
                    },
                    labelLine: {
                      show: false
                    }
                  }
                }
              }, {
                name: 'lanweihong',
                value: 100 - item.value
              }]
          }
        )
      })
      let option = {
        title: titleList,
        color: ['rgba(7, 158, 254, .9)'],
        series: seriesList
      }
      chart.setOption(option)
    }
  },
  watch: {
    data: {
      handler (newValue, oldValue) {
        if (oldValue != newValue) {
          this.setOptions()
        }
      },
      deep: true
    }
  }
}
</script> -->