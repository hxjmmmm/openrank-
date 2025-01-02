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
public class sumController {
    @Autowired
    private KddService kddService;
    @GetMapping("/sumOpenRank/{pojoname}")
    public Result list(@PathVariable String pojoname) {
        log.info("查询sumOpenRank");

        //查询sumOpenRank值
        sumOpenRank sumOpenRank=   kddService.sumOpenRank(pojoname);
        Map<String, Integer> sumOpenRankValue = new HashMap<>();
        sumOpenRankValue.put("clickCount", Integer.valueOf(sumOpenRank.getClickCount()));
        sumOpenRankValue.put("maxForks", Integer.valueOf(sumOpenRank.getMaxForks()));
        sumOpenRankValue.put("maxStars", Integer.valueOf(sumOpenRank.getMaxStars()));
        sumOpenRankValue.put("totalIssues", Integer.valueOf(sumOpenRank.getTotalIssues()));
        sumOpenRankValue.put("totalPulls", Integer.valueOf(sumOpenRank.getTotalPulls()));
        sumOpenRankValue.put("totalContributors", Integer.valueOf(sumOpenRank.getTotalContributors()));

        return Result.success(sumOpenRankValue);
    }
}
