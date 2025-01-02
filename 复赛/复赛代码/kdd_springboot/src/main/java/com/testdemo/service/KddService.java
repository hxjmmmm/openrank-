package com.testdemo.service;

import com.testdemo.pojo.*;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

public interface KddService {

    List<node> networklist(String pojoname);
    Map<String, Object> nodeMapArraylist(String pojoname);
    List<link> linkList(String pojoname);

    List<contributer> contributerList(String pojoname);

    List<issues> issuesList(String pojoname);

    List<pull> pullList(String pojoname);

    List<sumOpenRank> sumOpenRankList(String pojoname);

    Map<String, Object> contributerArrayList(String pojoname);

    sumOpenRank sumOpenRank(String pojoname);

    Map<String, Object> NodeLinks(String pojoname);


    List<warehouse> queryWareHouseList();

    Map<String, Object> pullArrayList(String pojoname);
}
