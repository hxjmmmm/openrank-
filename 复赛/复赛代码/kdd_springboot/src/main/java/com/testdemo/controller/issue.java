package com.testdemo.controller;

import com.testdemo.pojo.Result;
import com.testdemo.pojo.issues;
import com.testdemo.pojo.pull;
import com.testdemo.pojo.sumOpenRank;
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
public class issue {
    @Autowired
    private KddService kddService;
    @GetMapping("/IssueOpenRank/{pojoname}")
    public Result list(@PathVariable String pojoname) {
        log.info("查询issue值");
        List<issues> issuesList = kddService.issuesList(pojoname);
        Map<String, Object> openIssueList = new HashMap<>();
        // 初始化四个数组，用于存储提取的数据
        List<String> time = new ArrayList<>();
        List<Integer> issuesCreated = new ArrayList<>();
        List<Integer> issuesClosed = new ArrayList<>();
        for (issues issues : issuesList) {
            time.add(String.valueOf(issues.getTime()));
            issuesCreated.add(Integer.valueOf(issues.getIssuesCreated()));
            issuesClosed.add(Integer.valueOf(issues.getIssuesClosed()));
        }

        // 使用字符串作为键，数组作为值
        openIssueList.put("time", time);
        openIssueList.put("issuesCreated", issuesCreated);
        openIssueList.put("issuesClosed", issuesClosed);

        return Result.success(openIssueList);
    }
}
