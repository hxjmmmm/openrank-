package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class issues {
    private int id;
    private String repoId;
    private String repoName;//仓库名称
    private String    time;
    private String issuesCreated;
    private String issuesClosed;
}
