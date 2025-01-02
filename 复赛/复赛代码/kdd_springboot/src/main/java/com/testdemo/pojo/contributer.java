package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class contributer {
    private int id;
    private String repoId;  //仓库id
    private String repoName;//仓库名称
    private String actorId;//用户id
    private String actorLogin;//用户名
    private Integer activityCount;//用户数量
    private  Integer rank;//排序
}
