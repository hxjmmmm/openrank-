package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class sumOpenRank {
    private String repoId;
    private String repoName;//仓库名称
    private String clickCount;
    private String maxForks;
    private String maxStars;
    private String totalIssues;
    private String totalPulls;
    private String totalContributors;
}
