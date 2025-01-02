package com.testdemo.service.impl;
import com.testdemo.mapper.KddMapper;
import com.testdemo.pojo.*;
import com.testdemo.service.KddService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.*;

@Service
@Transactional
public class KddServiceImpl implements KddService {
    @Autowired
     KddMapper kddMapper;
    @Override
    public List<node> networklist(String pojoname) {
        return kddMapper.nodeList(pojoname);
    }

    @Override
    public Map<String, Object> nodeMapArraylist(String pojoname) {
        List<node> nodeList = kddMapper.nodeList(pojoname);
        //
        Map<String, Object> openContributerList = new HashMap<>();
        // 使用字符串作为键，数组作为值
        Integer[] array2 = {1550, 290, 380};
        String[] array1 = {"a", "b", "c"};
        openContributerList.put("provinceList", array1);
        openContributerList.put("valueList", array2);
        return openContributerList;
    }

    @Override
    public List<link> linkList(String pojoname) {
        return kddMapper.linkList(pojoname);
    }

    @Override
    public List<contributer> contributerList(String pojoname) {
        return kddMapper.contributerList(pojoname);
    }

    @Override
    public List<issues> issuesList(String pojoname) {
        return kddMapper.issuesList(pojoname);
    }

    @Override
    public List<pull> pullList(String pojoname) {
        return kddMapper.pullList(pojoname);
    }

    @Override
    public List<sumOpenRank> sumOpenRankList(String pojoname) {
        return kddMapper.sumOpenRankList(pojoname);
    }

    @Override
    public  Map<String,Object> contributerArrayList(String pojoname) {
        // 初始化provinceList和valueList数组
        List<String> provinceList = new ArrayList<>();
        List<Integer> valueList = new ArrayList<>();

        List<contributer> contributors = kddMapper.contributerList(pojoname);
        // 循环遍历contributors列表
        for (contributer contributor : contributors) {
            // 获取actorLogin和activityCount字段
            String actorLogin = contributor.getActorLogin();
            int activityCount = contributor.getActivityCount();

            // 将actorLogin添加到provinceList
            provinceList.add(actorLogin);

            // 将activityCount添加到valueList
            valueList.add(activityCount);
        }
        Map<String, Object> openContributerList = new HashMap<>();
        // 使用字符串作为键，数组作为值
        openContributerList.put("provinceList", provinceList);
        openContributerList.put("valueList", valueList);
        return openContributerList;
    }

    @Override
    public sumOpenRank sumOpenRank(String pojoname) {
        return kddMapper.sumOpenRank(pojoname);
    }


    @Override
    public Map<String, Object> NodeLinks(String pojoname) {
       List<node> nodes = kddMapper.nodeList(pojoname);
        List<links> link = kddMapper.linksList(pojoname);
        Map<String, Object> NodeLinksList = new HashMap<>();
        // 使用字符串作为键，数组作为值
        NodeLinksList.put("nodes", nodes);
        NodeLinksList.put("links", link);
        return NodeLinksList;
    }

    @Override
    public List<warehouse> queryWareHouseList() {
        List<warehouse> warehouses = kddMapper.queryWareHouseList();
        return warehouses;
    }

    @Override
    public Map<String, Object> pullArrayList(String pojoname) {
         //将pullList拆为四个数组
        List<pull> link = kddMapper.pullList(pojoname);
        Integer kdd=kddMapper.IfPojo(pojoname);
        // 初始化四个数组，用于存储提取的数据
        List<String> times = new ArrayList<>();
        List<Integer> pullsCreatedList = new ArrayList<>();
        List<Integer> pullsMergedList = new ArrayList<>();
        List<Double> processingEfficiencyList = new ArrayList<>();  // 遍历link列表，提取每个实体的属性
        for (pull pull : link) {
            times.add(String.valueOf(pull.getTime()));
            pullsCreatedList.add(pull.getPullsCreated());
            pullsMergedList.add(pull.getPullsMerged());
            processingEfficiencyList.add(pull.getProcessingEfficiency());
        }

        Map<String, Object> pullArrayList = new HashMap<>();
        // 使用字符串作为键，数组作为值
        pullArrayList.put("dateList", times);
        pullArrayList.put("pullsCreated", pullsCreatedList);
        pullArrayList.put("pullsMerged", pullsMergedList);
        pullArrayList.put("processingEfficiency", processingEfficiencyList);
        pullArrayList.put("kdd", kdd);
        return pullArrayList;
    }


}
