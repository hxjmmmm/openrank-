package com.testdemo.controller;

import com.testdemo.mapper.KddMapper;
import com.testdemo.pojo.Result;
import com.testdemo.service.KddService;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.annotations.Select;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.Map;
@Controller
@Slf4j
public class IfPojo {
    @Autowired
    private KddMapper kddMapper;
    @GetMapping("/IfPojo/{pojoname}")
    public Result IfPojo(@PathVariable String pojoname) {
        log.info("判断输入是否属于300仓库里面的值");
        Boolean result = false;
        Integer kdd=kddMapper.IfPojo(pojoname);
        if(kdd==1) result = true;
        return Result.success(result);
    }
}
