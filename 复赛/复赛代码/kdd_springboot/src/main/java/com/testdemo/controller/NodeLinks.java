package com.testdemo.controller;

import com.testdemo.pojo.Result;
import com.testdemo.service.KddService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@Slf4j
@RestController
public class NodeLinks {
    @Autowired
    private KddService kddService;
    @GetMapping("/NodeLinks/{pojoname}")
    public Result NodeLinks(@PathVariable String pojoname) {
        log.info("查询issue值");
      Map<String, Object> NodeLinks=kddService.NodeLinks(pojoname);

        return Result.success(NodeLinks);
    }
}
