package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class warehouse {
    private int id;
    private String repoName;
    private int maxStars;
    private  int maxForks;
    private  int openvalue;
}
