package com.testdemo.controller;

import com.testdemo.pojo.*;
import com.testdemo.service.KddService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@RestController
public class KddController {
    @Autowired
    private KddService kddService;
    @GetMapping("/kdd/{pojoname}")
    public Result list(@PathVariable String pojoname) {
        log.info("根据仓库id查询出网络结构贡献者排名，总数据表，pull处理请求，illsue，语言占比");
        //查询node集合
        List<node> nodeList=kddService.networklist(pojoname);

        //查询link集合
        List<link> linkList=kddService.linkList(pojoname);
        //查询贡献者集合
        List<contributer> contributerList=kddService.contributerList(pojoname);
        //查询issues集合
        List<issues> issuesList=kddService.issuesList(pojoname);
        //查询pull
        List<pull> pullList =kddService.pullList(pojoname);
        //查询sumOpenRank值
        List<sumOpenRank> sumOpenRankList =kddService.sumOpenRankList(pojoname);
        Integer[] array2 = {1550, 290, 380};
        String[] array1 = {"a", "b", "c"};
        List openList=new ArrayList();
        // 创建Map集合
        Map<String, Object> openContributerList = new HashMap<>();
        // 使用字符串作为键，数组作为值
        openContributerList.put("provinceList", array1);
        openContributerList.put("valueList", array2);
        return Result.success(openContributerList);
    }
}
