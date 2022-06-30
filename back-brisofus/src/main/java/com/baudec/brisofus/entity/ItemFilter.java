package com.baudec.brisofus.entity;

import lombok.*;

import java.util.List;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@ToString
public class ItemFilter {

    public String searchName;
    public int levelMin;
    public int levelMax;
    public List<String> listAttribute;
    public List<String> listType;


}
