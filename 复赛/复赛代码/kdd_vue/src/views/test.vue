<template>
  <div class="container">
    <!-- 顶部 -->
    <div class="top-header">
  
        <div class="title">
       
                <h1>{{ title }}</h1>
       
       
            <div class="top-header-tip">
            <div class="sub-title">
              此数据为实时真实数据，数据来源：openrank
            </div>
            <div class="last-update-time">
              更新时间：{{ "2024-12-15 20:39:11" }}
            </div>
          </div>
   
          
        </div>
   
    </div>
    <div class="main-content">
          <!-- 中间信息开始 -->
          <div class="statistics-content">
            <!-- 中间左侧开始 -->
            <div class="main-inner">
                  <chart-card
                    title="贡献者排名（TOP 10）"
                    :customClass="`chart-item-bottom-sep`"
                  >
                    <province-ranking-bar-chart
                      ref="topConfirmedCountRankChart"
                      :data="top10ProvinceData"
                      style="width: 100%; height: 380px"
                    />
                  </chart-card>
                  <!-- 占比 -->
                  <chart-card
                    title="语言占比"
                    :customClass="`chart-item-bottom-sep`"
                  >
                    <basic-proportion-chart
                      ref="basicProportionChart"
                      :data="basicData"
                      style="width: 100%; height: 120px"
                    />
                  </chart-card>
                  <chart-card title="issue新增、关闭数量">
                    <current-confirmed-compare-bar-chart
                      ref="confirmSingleBarChart"
                      :issueTime="issueTime"
                      :issuesCreated="issuesCreated"
                      :issuesClosed="issuesClosed"
                      style="width: 100%; height: 310px"
                    />
                  </chart-card>
                  <!-- 顶部基本统计信息开始 -->
                  <div class="basic-header flex">
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
            </div>
            <!-- 中间左侧结束 -->
          </div>
          <!-- 中间信息结束 -->
      
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
              />
              <i class="el-icon-search"></i>
            </div>
            <chart-card title="" :customClass="`chart-item-bottom-sep`">
              <div slot="title" class="province-table-title flex">
                仓库排名
                <el-link
                  icon="el-icon-view"
                  style="color: #bcbcbf; padding-left: 10px"
                  :underline="false"
                  @click="provinceTableDialogShowHandler"
                  >详情</el-link
                >
              </div>
              <dv-scroll-board
                :config="provinceConfirmedCountBoardConfig"
                style="width: 100%; height: 360px"
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
                style="width: 100%; height: 520px"
              />
            </chart-card>
          </div>
          <!-- 右侧区域结束 -->
  
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
  
  <style>
/* 根容器设置 */
.container {
  width: 100%;
  padding: 10px;
}

/* 顶部标题 */
.top-header {
  text-align: left;
  margin-bottom: 20px;
}

.top-header h1 {
  font-size: 28px;
  font-weight: bold;
}

.top-header-tip {
  font-size: 14px;
  color: #666;
}

/* 主体内容布局 */
.main-content {
  display: flex;
  flex-wrap: wrap;
}

/* 主区域左侧 */
.main-left {
  padding: 10px;
}

.left-column {
  display: flex;
  flex-direction: column;
}

.chart-item {
  background: #0f142b;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}

/* 地图容器 */
.main-inner-map-wrapper {
  padding: 20px;
  border-radius: 10px;
}

.map {
  height: 70vh; /* 高度自适应 */
  width: 100%;
}

/* 右侧区域 */
.main-right {
  padding: 10px;
}

.search-container {
  margin-bottom: 20px;
}

.search-input {
  width: calc(100% - 30px);
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
}
.el-col {
  flex: 1 1 auto;
}
/* 响应式布局 */
@media (max-width: 768px) {
  .main-content {
    flex-direction: column;
  }

  .main-left,
  .main-right {
    flex: 100%;
  }

  .map {
    height: 50vh; /* 小屏幕地图缩小 */
  }
}

@media (min-width: 1200px) {
  .map {
    height: 90vh; /* 大屏幕地图扩展 */
  }
}
</style>
  