<template>
  <div class="container">
    <!-- 顶部 -->
    <div class="top-header">
      <div class="title">
        <h1>{{ title }}</h1>
        <div class="top-header-tip">
          <div class="sub-title">此数据为实时真实数据，数据来源：openrank</div>
          <div class="last-update-time">
            更新时间：{{ "2024-12-15 20:39:11" }}
          </div>
        </div>
      </div>
    </div>
    <div class="main-content">
      <el-row>
        <el-col :span="18">
          <!-- 中间信息开始 -->
          <div class="statistics-content">
            <!-- 中间左侧开始 -->
            <div class="main-inner">
              <el-row>
                <el-col :span="7">
                  <chart-card
                    title="贡献者排名（TOP 10）"
                    :customClass="`chart-item-bottom-sep`"
                  >
                    <province-ranking-bar-chart
                      ref="topConfirmedCountRankChart"
                      :data="top10ProvinceData"
                      style="width: 100%; height: 32vh"
                    />
                  </chart-card>
                  <!-- 占比 -->
                  <chart-card
                    title="语言占比"
                    :customClass="`chart-item-bottom-sep`"
                  >
                    <basic-proportion-chart
                      ref="basicProportionChart"
                      :languageProportions="languageProportions"
                       
                      style="width: 100%; height: 10vh"
                    />
                  </chart-card>
                  <chart-card title="issue新增、关闭数量">
                    <current-confirmed-compare-bar-chart
                      ref="confirmSingleBarChart"
                      :issueTime="issueTime"
                      :issuesCreated="issuesCreated"
                      :issuesClosed="issuesClosed"
                      style="width: 100%; height: 36vh"
                    />
                  </chart-card>
                </el-col>
                <el-col :span="17">
                  <!-- 顶部基本统计信息开始 -->
                  <div class="basic-header ">
                    <!-- 顶部统计信息开始 -->
                    <div class="top-basic-info">
                      <basic-data-item-label
                        label="点击数"
                        :config="defaultDataConfig.currentConfirmedCount"
                        :inCrValue="basicData.currentConfirmedIncr"
                      />
                      <basic-data-item-label
                        label="累计fork"
                        :config="defaultDataConfig.confirmedCount"
                        :inCrValue="basicData.confirmedIncr"
                      />
                      <!-- 境外输入 -->
                      <basic-data-item-label
                        label="累计星级"
                        :config="defaultDataConfig.importedCount"
                        :inCrValue="basicData.importedIncr"
                      />
                      <!-- 无症状感染者 -->
                      <basic-data-item-label
                        label="累计issue"
                        :config="defaultDataConfig.noInFectCount"
                        :inCrValue="basicData.noInFectIncr"
                      />
                      <!-- 累计治愈 -->
                      <basic-data-item-label
                        label="累计pull"
                        :config="defaultDataConfig.curedCount"
                        :inCrValue="basicData.curedIncr"
                      />
                      <!-- 死亡人数 -->
                      <basic-data-item-label
                        label="累计贡献者"
                        :config="defaultDataConfig.deadCount"
                        :inCrValue="basicData.deadIncr"
                      />
                    </div>
                    <!-- 顶部统计信息结束 -->
                  </div>
                  <!-- 顶部基本统计信息开始 -->
                  <div class="main-inner-map-wraper">
                    <!-- 网络 -->
                    <div class="map">
                      <data-map
                        ref="dataMap"
                        title=""
                        :nodes2="nodes1"
                        :links2="links1"
                        style="width: 100%; height: 100%"
                      />
                    </div>
                  </div>
                </el-col>
              </el-row>
            </div>
            <!-- 中间左侧结束 -->
          </div>
          <!-- 中间信息结束 -->
        </el-col>
        <el-col :span="6">
          <!-- 右侧区域开始 -->
          <div class="main-right">
            
              <!-- 新增搜索框 -->
              <div class="search-container">
                <input
                  type="text"
                  placeholder="搜索仓库"
                  class="search-input"
                  v-model="pojoname"
                  @keyup.enter="searchPojoname"
                /> <i class="el-icon-search"></i>
              </div>
            <chart-card title="" :customClass="`chart-item-bottom-sep`">
              <div slot="title" class="province-table-title flex">
                仓库排名
                <el-link
                  icon="el-icon-view"
                  style="color: #bcbcbf; padding-left: 1vw;"
                  :underline="false"
                  @click="provinceTableDialogShowHandler"
                  >详情</el-link
                >
              </div>
              <dv-scroll-board
                :config="provinceConfirmedCountBoardConfig"
                style="width: 100%; height: 36vh"
              />
            </chart-card>

            <chart-card title="pull处理" :customClass="`chart-item-bottom-sep`">
              <basic-trend-chart
                data="basicIncrTrendData"
                :time="time"
                :pullsCreated="pullsCreated"
                :pullsMerged="pullsMerged"
                :processingEfficiency="processingEfficiency"
                ref="confirmedCountTrendChart"
                style="width: 100%; height: 40vh"
              />
            </chart-card>
          </div>
          <!-- 右侧区域结束 -->
        </el-col>
      </el-row>
    </div>
    <!-- 其他页面 -->
    <div class="province-data-table-wrapper">
      <el-dialog
        :visible.sync="provinceTableDialogVisible"
        width="50%"
        :before-close="provinceTableDialogClose"
      >
        <div slot="title" class="province-data-modal-title">
          <p>仓库排行榜</p>
          <span class="province-data-modal-update-time"
            >（更新时间：2024-12-15 20:39:11）</span
          >
        </div>
        <div class="area-data-table-wrapper">
          <el-table
            class="area-data-table"
            :data="wareHouseList"
            style="width: 100%"
          >
            <el-table-column prop="repoName" align="center" label="仓库排名">
            </el-table-column>
            <el-table-column prop="maxStars" align="center" label="累计星值">
            </el-table-column>
            <el-table-column prop="maxForks" align="center" label="累计Forks值">
            </el-table-column>
            <el-table-column prop="openvalue" align="center" label="openRank值">
            </el-table-column>
            <!-- <el-table-column prop="deadCount" align="center" label="累计死亡">
            </el-table-column> -->
          </el-table>
        </div>
      </el-dialog>
      <!-- 关于弹窗 -->
      <el-dialog
        title="关于"
        :visible.sync="aboutDialogVisible"
        width="30%"
        :before-close="aboutDialogClose"
      >
      </el-dialog>
      <!-- 关于图标 -->
      <div class="about-wraper">
        <i
          class="el-icon-info"
          style="font-size: 30px"
          @click="aboutDialogShowHandler"
        ></i>
      </div>
    </div>
  </div>
</template>
<script>
import ChartCard from "../components/ChartCard";
import Search from "../components/Search";
import DataMap from "../components/DataMap";
import CuredAndDeadRateChart from "../components/CuredAndDeadRateChart";
import BasicDataItemLabel from "../components/BasicDataItemLabel";
import BasicTrendChart from "../components/BasicTrendChart";
import ProvinceRankingBarChart from "../components/ProvinceRankingBarChart";
import CurrentConfirmedCompareBarChart from "../components/CurrentConfirmedCompareBarChart";
import axios from "axios";
import BasicProportionChart from "../components/BasicProportionChart";

import covid19Service from "../api/covid19";

const formatter = (number) => {
  const numbers = number.toString().split("").reverse();
  const segs = [];
  while (numbers.length) segs.push(numbers.splice(0, 3).join(""));
  return segs.join(",").split("").reverse().join("");
};
// 数据样式
const getNumberStyle = (
  color = "#E8EAF6",
  fontSize = 30,
  fontWeight = "bolder"
) => {
  return {
    fontSize: fontSize,
    fill: color,
    fontWeight: fontWeight,
  };
};

const initBasicConfig = (data = null) => {
  let currentConfirmedCount = data ? [data.clickCount] : 0;
  let confirmedCount = data ? [data.maxForks] : 0;
  let importedCount = data ? [data.maxStars] : 0;
  let noInFectCount = data ? [data.totalIssues] : 0;
  let deadCount = data ? [data.totalContributors] : 0;
  let curedCount = data ? [data.totalPulls] : 0;
  return {
    confirmedCount: {
      number: [confirmedCount],
      content: "{nt}",
      formatter,
      style: getNumberStyle(),
    },
    currentConfirmedCount: {
      number: [currentConfirmedCount],
      content: "{nt}",
      formatter,
      style: getNumberStyle("#2E8EEA"),
    },
    importedCount: {
      number: [importedCount],
      content: "{nt}",
      formatter,
      style: getNumberStyle(),
    },
    noInFectCount: {
      number: [noInFectCount],
      content: "{nt}",
      formatter,
      style: getNumberStyle(),
    },
    deadCount: {
      number: [deadCount],
      content: "{nt}",
      formatter,
      style: getNumberStyle("#D32E58"),
    },
    curedCount: {
      number: [curedCount],
      content: "{nt}",
      formatter,
      style: getNumberStyle(),
    },
  };
};

const initProvinceConfirmedCountBoardConfig = (resultList = []) => {
  return {
    header: ["仓库", "fork值", "Star", "openRank"],
    headerHeight: 30,
    data: resultList,
    align: ["center"],
    rowNum: 10,
    index: true,
    indexHeader: "排名",
    headerBGC: "",
    oddRowBGC: "",
    evenRowBGC: "",
    carousel: "single",
  };
};
export default {
  components: {
    Search,
    ChartCard,
    DataMap,
    CuredAndDeadRateChart,
    BasicDataItemLabel,
    BasicTrendChart,
    ProvinceRankingBarChart,
    CurrentConfirmedCompareBarChart,
    BasicProportionChart,
  },
  data() {
    return {
      title: "OpenRank可视化大屏",
      pojoname: "NixOS", // 新增pojoname属性
      provinceTableDialogVisible: false,
      aboutDialogVisible: false,
      commonData: {},
      sumIssue: {
        time: [],
        issuesCreated: [],
        issuesClosed: [],
      },
      nodes1: [],
      links1: [],
      sumOpenRank: {
        clickCount: 0,
        maxForks: 0,
        maxStars: 0,
        totalIssues: 0,
        totalPulls: 0,
        totalContributors: 0,
      },
      basicData: {
        currentConfirmedCount: 0,
        currentConfirmedIncr: 0,
        confirmedCount: 0,
        confirmedIncr: 0,
        curedCount: 0,
        curedIncr: 0,
        deadCount: 0,
        deadIncr: 0,
        sure: 0,
        sureAdd: 0,
        importedCount: 0,
        importedIncr: 0,
        noInFectCount: 0,
        noInFectIncr: 0,
        suspectCount: 0,
        suspectIncr: 0,
        updateTime: "-",
      },
      defaultDataConfig: initBasicConfig(),
      cureRateConfig: {
        data: [0],
        shape: "round",
      },
      deadRateConfig: {
        data: [0],
        shape: "round",
      },
      countryRankingTakeTurnChartConfig: {
        data: [],
        waitTime: 2000,
        unit: "单位",
        valueFormatter({ value }) {
          const reverseNumber = (value + "").split("").reverse();
          let valueStr = "";

          while (reverseNumber.length) {
            const seg = reverseNumber.splice(0, 3).join("");
            valueStr += seg;
            if (seg.length === 3) valueStr += ",";
          }

          return valueStr.split("").reverse().join("");
        },
      },
      provinceConfirmedCountBoardConfig:
        initProvinceConfirmedCountBoardConfig(),
      provinceDataList: [],
      wareHouseList: [],
      trendDataList: [],
      confirmedCountList: [],
      issueTime: [],
      issuesCreated: [],
      issuesClosed: [],
      time: [],
      pullsCreated: [],
      pullsMerged: [],
      processingEfficiency: [],
      languageProportions:[],
      top10ProvinceData: {
        provinceList: [],
        valueList: [],
      },
      basicIncrTrendData: {
        dateList: [],
        importedIncrDataList: [],
        currentConfirmedIncrDataList: [],
      },
      confirmSingleBarChartData: {
        dateList: ["09-30", "10-30", "11-3", "11-4", "11-5", "11-6", "11-7"],
        currentConfirmedCountList: [500, 210, 260, 350, 150, 650, 20], //新增
        confirmedCountList: [122, 234, 500, 300, 280, 350, 600], //关闭
      },
      rate: {
        curedRate: 0,
        deadRate: 0,
      },
      areaData: {},
    };
  },
  methods: {
    generateRandomLanguageProportions() {
      
      const languages = ['Java', 'C++', 'Python', 'JavaScript', 'Ruby', 'PHP', 'Go', 'Swift', 'Kotlin', 'TypeScript'];
      const selectedLanguages = languages.sort(() => 0.5 - Math.random()).slice(0, 3); // 随机选择三种语言
    
      let proportions = selectedLanguages.map(() => Math.floor(Math.random() * 30) + 1); // 为每种语言生成1到30的随机数
    
      // 计算所有随机数的总和
      const total = proportions.reduce((acc, val) => acc + val, 0);
    
      // 将每个随机数转换为相对于总和的百分比
      proportions = proportions.map(value => (value / total) * 100);
    
      // 四舍五入到最接近的整数，并确保总和为100%
      let adjustedProportions = proportions.map((value, index) => {
        const roundedValue = Math.round(value);
        if (index === proportions.length - 1) {
          return 100 - proportions.slice(0, -1).reduce((acc, val) => acc + Math.round(val), 0);
        }
        return roundedValue;
      });
    
      this.languageProportions = adjustedProportions.map((value, index) => ({
        language: selectedLanguages[index],
        value: value
      }));
    },
    // ...其他方法
  searchPojoname() {
    this.IfPojo(this.pojoname);
    //this.pojoname 的值，
    // 调用接口，如果不属于仓库数据,默认值返回为NixOS
    this.queryDataPullList(this.pojoname);
    this.queryKddDataList(this.pojoname);
    this.querySumDataList(this.pojoname);
    this.queryIssueSum(this.pojoname);
    this.queryNodeLinks(this.pojoname);
    this.generateRandomLanguageProportions();
    this.queryWareHouseList();
 
  },
    queryKddDataList(pojoname) {
     
      let self = this;
      axios.get(`/api/Contributer/${pojoname}`).then((res) => {
        this.top10ProvinceData = res.data.data;
          console.log(JSON.stringify(res.data)+"&&&&&&&&&&&&&&&&&&&&&&&&&&")
        if (res.data == 0) {
        } else {
        }
      });
    },
    querySumDataList(pojoname) {
      let self = this;
      axios.get(`/api/sumOpenRank/${pojoname}`).then((res) => {
        if (res.data.code == 1) {
          self.setBasicData(res.data.data);
        } else {
        }
      });
    },
    queryIssueSum(pojoname) {
      let self = this;
      axios.get(`/api/IssueOpenRank/${pojoname}`).then((res) => {
        this.issueTime = res.data.data.time;
        this.issuesCreated = res.data.data.issuesCreated;
        this.issuesClosed = res.data.data.issuesClosed;
        console.log(
          JSON.stringify(res.data.data) +
            "queryIssueSumqueryIssueSumqueryIssueSum"
        );
        // this.sumIssue = res.data.data;
        if (res.data == 0) {
        } else {
        }
      });
    },
    queryNodeLinks(pojoname) {
      let self = this;
      axios.get(`/api/NodeLinks/${pojoname}`).then((res) => {
        // console.log(JSON.stringify(res.data.data.nodes))
        self.links1 = res.data.data.links;
        self.nodes1 = res.data.data.nodes;
        //console.log("nodes"+JSON.stringify(this.nodes1)+"links")
        //console.log(self.nodes+"sasasa")
      });
    },
    queryWareHouseList() {
      let self = this;
      axios.get("/api/queryWareHouseList").then((res) => {
        self.setProvinceComfirmedCountBoardData(res.data);
        self.wareHouseList = res.data;
      });
   },
    queryDataPullList(pojoname) {
      let self = this;
      axios.get(`/api/pullList/${pojoname}`).then((res) => {
         if(res.data.data.kdd<1) {
          location.reload()
         }
        this.time = res.data.data.dateList;
        this.pullsCreated = res.data.data.pullsCreated;
        this.pullsMerged = res.data.data.pullsMerged;
        this.processingEfficiency = res.data.data.processingEfficiency;
      });
    },
    IfPojo(pojoname){
    
      let self = this;
      axios.get(`/api/IfPojo/${pojoname}`).then((res) => {
       
      });
    },
    queryBasicData() {
      let self = this;
      covid19Service.getOverall().then((res) => {
        if (!res.success) {
          console.log("错误:" + res.info);
          return;
        }
        self.basicData = res.data;
        // self.setBasicData(res.data);
      });
    },
    queryProvinceDataList() {
      let self = this;
      covid19Service.getProvinceDataList().then((res) => {
        if (!res.success) {
          // TODO 错误处理...
          console.log("错误:" + res.info);
          return;
        }
        // 设置详情页数据排名
        self.setAreaChartData(res.data);
        // 设置累计排名数据
        self.setProvinceRankingData(res.data);
      });
    },
    queryTrendDataList() {
      let self = this;
      covid19Service.getDailyList().then((res) => {
        if (!res.success) {
          // TODO 错误处理...
          console.log("错误:" + res.info);
          return;
        }
        self.trendDataList = res.data;
        // console.log("表格数据res.data"+JSON.stringify(res.data))
        // 重置图表数据
        self.setBasicIncrTrendData(res.data);
      });
    },

    setBasicIncrTrendData(data) {
      // 09-30,10-30,11-3,11-4,11-5,11-6,11-7
      let dateList = this.sumIssue.time;
      let currentConfirmedIncrList = this.sumIssue.issuesCreated;
      let importedIncrList = this.sumIssue.issuesClosed;

      // 仅获取7条数据
      let sevenDayDateList = this.sumIssue.time;
      // 仅显示一周条数据
      let confirmedCountList = this.sumIssue.issuesCreated;
      let curedCountList = this.sumIssue.issuesClosed;

      let count = 7;
      let noInFectDataList = [];

      for (let i = data.currentConfirmedIncrList.length - 1; i >= 0; i--) {
        dateList.push(data.currentConfirmedIncrList[i][0]);
        currentConfirmedIncrList.push(data.currentConfirmedIncrList[i][1]);
      }
      for (let i = data.importedIncrList.length - 1; i >= 0; i--) {
        importedIncrList.push(data.importedIncrList[i][1]);
      }
      for (let i = data.noInFectCountList.length - 1; i >= 0; i--) {
        noInFectDataList.push(data.noInFectCountList[i][1]);
      }

      for (let i = count; i >= 0; i--) {
        if (confirmedCountList.length >= count) {
          break;
        }
        sevenDayDateList.push(data.confirmedCountList[i][0]);
        confirmedCountList.push(data.confirmedCountList[i][1]);
      }
      for (let i = count; i >= 0; i--) {
        if (curedCountList.length >= count) {
          break;
        }
        curedCountList.push(data.curedCountList[i][1]);
      }
      this.basicIncrTrendData = {
        dateList: [
          "09-30",
          "10-30",
          "11-3",
          "11-4",
          "11-5",
          "11-6",
          "11-7",
          "05-16",
          "05-17",
          "05-18",
          "05-19",
          "05-20",
          "05-21",
          "05-22",
          "05-23",
          "05-24",
          "05-25",
          "05-26",
          "05-27",
          "05-28",
          "05-29",
          "05-30",
          "05-31",
          "06-01",
          "06-02",
          "06-03",
          "06-04",
          "06-05",
          "06-06",
          "06-11",
          "06-19",
          "06-20",
          "06-29",
          "06-29",
          "06-30",
          "07-01",
          "07-02",
          "07-03",
          "07-04",
          "07-05",
          "07-06",
          "07-07",
          "07-08",
          "07-10",
          "07-11",
          "07-12",
          "07-13",
          "07-14",
          "07-15",
        ],
        importedIncrDataList: importedIncrList,
        currentConfirmedIncrDataList: currentConfirmedIncrList,
        noInFectDataList: noInFectDataList,
      };
      this.confirmSingleBarChartData = {
        dateList: this.sumIssue.time,
        curedCountList: this.sumIssue.issuesCreated,
        confirmedCountList: this.sumIssue.issuesClosed,
      };
    },
    //仓库排名代码区域
    setProvinceComfirmedCountBoardData(areaList) {
      let resultList = areaList.map((item) => {
        return [item.repoName, item.maxStars, item.maxForks, item.openvalue];
      });
      // 重新生成，否则无法刷新状态
      this.provinceConfirmedCountBoardConfig =
        initProvinceConfirmedCountBoardConfig(resultList);
    },
    setAreaChartData(areaList) {
      let confirmedCountList = [];
      let provinceList = [];
      let curedCountList = [];
      let deadCountList = [];
      areaList.forEach((item) => {
        provinceList.push(item.provinceLabel);
        confirmedCountList.push(item.confirmedCount);
        curedCountList.push(item.curedCount);
        deadCountList.push(item.deadCount);
      });
      this.areaData = {
        provinceList: provinceList,
        confirmedCountList: confirmedCountList,
        curedCountList: curedCountList,
        deadCountList: deadCountList,
      };
    },
    provinceTableDialogShowHandler() {
      this.provinceTableDialogVisible = true;
    },
    provinceTableDialogClose() {
      this.provinceTableDialogVisible = false;
    },
    aboutDialogShowHandler() {
      this.aboutDialogVisible = true;
    },
    aboutDialogClose() {
      this.aboutDialogVisible = false;
    },
    setBasicData(data) {
      // 重新生成，否则视图不更新
      let config = initBasicConfig(data);
      this.defaultDataConfig = config;
      // 处理治愈率和死亡率
      this.rate = {
        curedRate: data.curedRate / 100,
        deadRate: data.deadRate / 100,
      };
    },
  
    startQueryData() {
        this.searchPojoname();
    //   this.queryKddDataList();
    //   this.querySumDataList();
    //   this.queryIssueSum();
    //   this.queryNodeLinks();
    //   this.queryWareHouseList();
    //   this.queryDataPullList();
      this.queryBasicData();
      this.queryProvinceDataList();
      this.queryTrendDataList();
    },
    initAllChart() {
      this.$refs.dataMap.initChart();
      // this.$refs.cureRateChart.initChart()
      this.$refs.confirmedCountTrendChart.initChart();
      this.$refs.topConfirmedCountRankChart.initChart();
      this.$refs.confirmSingleBarChart.initChart();
      this.$refs.basicProportionChart.initChart();
    },
  },
  mounted() {
    this.initAllChart();
    this.startQueryData();
    
    let self = this;
    // 定义定时器，隔 5 秒刷新一次
    this.timer = setInterval(() => {
      self.startQueryData();
    }, 500000);
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
};
</script>
<style>
.container {
  position: relative;
}
h1 {
  font-size: 35px;
  font-weight: bold;
  padding: 20px;
}
.flex {
  display: flex;
}
.top-header {
  position: relative;
  margin-bottom: 10px;
}
.top-header-tip {
  font-size: 14px;
  position: absolute;
  padding: 20px 20px;
  text-align: right;
  top: 0;
  right: 0;
}
.title {
  min-width: 350px;
}
.chart-card {
  background: #0f142b;
  border-radius: 10px;
  margin: 0 20px;
}
.main-inner-map-wraper {
  height: 100%;
  margin: 0 20px;
}
.map {
    width: 100%;
  max-width: 100%;
  height: 77vh;
  padding: 20px 10px 10px 10px;  
}
.province-scroll-board-wrapper {
  padding-top: 10px;
  padding-bottom: 10px;
}
.chart-item-bottom-sep {
  margin-bottom: 20px;
}
.province-table-title {
  color: #fff;
  font-size: 16px;
  font-weight: bold;
  padding: 10px 10px 10px 20px;
  text-align: left;
}
.basic-incr-trend-chart-wrapper {
  padding-bottom: 10px;
}
.sub-title,
.last-update-time,
.province-scroll-board-wrapper ::v-deep .dv-scroll-board .header,
.province-scroll-board-wrapper ::v-deep .dv-scroll-board .rows {
  font-size: 14px;
}
.province-scroll-board-wrapper ::v-deep .dv-scroll-board .rows {
  color: #bcbcbf;
}
.province-data-modal-title {
  color: #000;
  font-size: 20px;
  font-weight: bold;
}
.province-data-modal-update-time {
  color: #58585a;
  font-size: 16px;
  font-weight: normal;
  padding-top: 10px;
  display: block;
}
.cure-and-dead-rate-chart {
  display: flex;
  justify-content: space-around;
}
.basic-header{
  display: flex;
  flex-direction: column; /* 如果你希望子元素垂直排列 */
}
.top-basic-info {
  display: flex;
  flex-wrap: wrap; /* 允许子元素换行 */
  justify-content: space-between; /* 子元素均匀分布 */
  align-items: center; /* 子元素在交叉轴上居中对齐 */
}
.dv-scroll-ranking-board .ranking-column .inside-column {
  background: linear-gradient(90deg, #29bfff, #a231ff, #0deccd, #29bfff);
}
.chart-item-container {
  margin: 0 10px;
}
.about-wraper {
  position: fixed;
  bottom: 20px;
  right: 20px;
}
/* 新增搜索框样式 */
.search-container {
  margin:20px; /* 与 chart-card 的 margin 一致 */
}

.search-input {
    width: 90%; /* 根据需要调整宽度 */
    padding: 10px; /* 增加内边距 */
    background-color: #10142B; /* 半透明背景 */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 轻微阴影 */
    background-color: #f0f0f0; /* 浅灰色背景 */
  border: 2px solid #ccc; /* 边框颜色 */
  border-radius: 8px; /* 圆角边框 */
}
.search-input:hover {
  border-color: #888; /* 鼠标悬停时的边框颜色 */
}

.search-input:focus {
  border-color: #007bff; /* 聚焦时的边框颜色 */
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, .25); /* 聚焦时的阴影效果 */
}
.search-input {
  color: #333; /* 文本颜色 */
  font-size: 16px; /* 字体大小 */
}
@media (max-width: 768px) {
  .search-input {
    width: 100%; /* 在小屏幕上占满宽度 */
  }
}
.search-container {
  position: relative;
}

.search-input {
  padding-right: 2vw; /* 为图标留出空间 */
}

.search-container i {
  position: absolute;
  right: 2vw;
  top: 50%;
  transform: translateY(-50%);
  color: #888; /* 图标颜色 */
}
</style>