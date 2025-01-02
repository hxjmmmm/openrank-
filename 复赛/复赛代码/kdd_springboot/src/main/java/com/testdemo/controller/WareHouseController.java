package com.testdemo.controller;

import com.testdemo.mapper.KddMapper;
import com.testdemo.pojo.Result;
import com.testdemo.pojo.warehouse;
import com.testdemo.service.KddService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@Controller
public class WareHouseController {

    @Autowired
    private KddMapper kddMapper;
    @Autowired
    private KddService kddService;
    @GetMapping("/queryWareHouseList")
    @ResponseBody
    public List<warehouse> queryWareHouseList() {
        log.info("查询仓库排名");
        List<warehouse> warehouseList=  kddService.queryWareHouseList();
        return warehouseList;
    }

}
