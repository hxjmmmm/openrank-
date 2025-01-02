package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class pull {
    private Integer id;
    private String time;
    private Integer repoId;
    private String repoName;//仓库名称
    private Integer pullsCreated;
    private Integer pullsMerged;
    private Double processingEfficiency;
}
