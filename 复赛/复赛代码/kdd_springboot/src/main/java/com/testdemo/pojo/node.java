package com.testdemo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class node{
  private   int id;
  private String name;
  private  double symbolSize;
  private double x;
  private double y;
  private String value;
  private int category;
}
