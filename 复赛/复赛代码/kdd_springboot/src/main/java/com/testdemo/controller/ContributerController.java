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
public class ContributerController {
    @Autowired
    private KddService kddService;
    @GetMapping("/Contributer/{pojoname}")
    public Result list(@PathVariable String pojoname) {
        log.info("返回两个贡献者数组");

        Map<String, Object> contributerArrayList=kddService.contributerArrayList(pojoname);

        return Result.success(contributerArrayList);
    }
}
