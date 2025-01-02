package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class link {
    private int id;
    private String repoName;//仓库名称
    private int source;
    private int target;
}
