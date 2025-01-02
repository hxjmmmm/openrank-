package com.testdemo.mapper;

import com.testdemo.pojo.*;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface KddMapper {

    List<node> nodeList(String pojoname);


    List<link> linkList(String pojoname);
    @Select("select * from contributer  where repo_name=#{pojoname} order by activity_count desc  limit  10 " )
    List<contributer> contributerList(String pojoname);
    @Select("select * from issues where repo_name=#{pojoname}")
    List<issues> issuesList(String pojoname);
    @Select("select * from  pull where repo_name=#{pojoname}")
    List<pull> pullList(String pojoname);
    @Select("select * from sumopenrank where repo_name=#{pojoname}")
    List<sumOpenRank> sumOpenRankList(String pojoname);
    @Select("select * from sumopenrank where repo_name=#{pojoname} limit 1" )
    sumOpenRank sumOpenRank(String pojoname);

    List<links> linksList(String pojoname);

   @Select("select * from node")
    List<node> nodeLists();

   @Select("select * from warehouse")
    List<warehouse> queryWareHouseList();
   @Select("SELECT COUNT(1) from warehouse where repo_name=#{pojoname} ")
    Integer IfPojo(String pojoname);
}
