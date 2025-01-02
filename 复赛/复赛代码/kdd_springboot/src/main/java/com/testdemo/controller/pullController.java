package com.testdemo.controller;

import com.testdemo.mapper.KddMapper;
import com.testdemo.pojo.Result;
import com.testdemo.service.KddService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;


@Slf4j
@RestController
public class pullController {
    @Autowired
    private KddService kddService;
    @Autowired
    private KddMapper kddMapper;
    @GetMapping("/pullList/{pojoname}")
    public Result list(@PathVariable String pojoname) {

        log.info("返回四个数组，用于pull请求");
        Map<String, Object> pullArrayList = kddService.pullArrayList(pojoname);
        return Result.success(pullArrayList);
    }
}