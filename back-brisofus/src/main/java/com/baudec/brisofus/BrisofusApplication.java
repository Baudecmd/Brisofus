package com.baudec.brisofus;

import com.baudec.brisofus.entity.Item;
import com.baudec.brisofus.repository.ItemRepository;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.*;
import org.json.JSONException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;


@SpringBootApplication
public class BrisofusApplication {
	@Autowired
	ItemRepository itemRepository;

	public static void main(String[] args) {
		SpringApplication.run(BrisofusApplication.class, args);
	}



	@EventListener(ApplicationReadyEvent.class)
	public void doSomethingAfterStartup() throws IOException, JSONException {
		/*System.out.println("debut ressources");
		EquipmentResources equipmentResources=new EquipmentResources("src/main/resources/file_v2/resources.json");
		itemRepository.saveAll(equipmentResources.getAllItem2());

		System.out.println("debut equipments");
		 equipmentResources=new EquipmentResources("src/main/resources/file_v2/equipments.json");
		itemRepository.saveAll(equipmentResources.getAllItem2());

		System.out.println("debut weapons");
		equipmentResources=new EquipmentResources("src/main/resources/file_v2/weapons.json");
		itemRepository.saveAll(equipmentResources.getAllItem2());


		System.out.println("hello c terminé");

		EquipmentParsing equipmentParsing=new EquipmentParsing("src/main/resources/file_v2/test_data.json");

		itemRepository.saveAll(equipmentParsing.getItems());*/

	}

	public class EquipmentParsing{
		public String filePath;
		public EquipmentParsing(String filePath) {
			this.filePath = filePath;
		}

		public List<Item> getItems() throws IOException {
			String jsonString=new String(Files.readAllBytes(Paths.get(filePath)));
			ObjectMapper objectMapper = new ObjectMapper();
			ItemRep[] itemReps = objectMapper.readValue(jsonString, ItemRep[].class);
			for(ItemRep itemRep:itemReps){
				System.out.println(itemRep);
			}
			return Arrays.stream(itemReps).map(elem->new Item(elem)).toList();


		}

		@Getter
		@Setter
		@JsonIgnoreProperties(ignoreUnknown = true)
		@ToString
		@NoArgsConstructor
		@AllArgsConstructor
		public static class ItemRep{
			int item_id;
			String item_name;
			List<ResourceRep> list_craft;
			List<StatValue> list_stat;
			int level;
			String item_type;
			int img_id;


		}

		@Getter
		@Setter
		@JsonIgnoreProperties(ignoreUnknown = true)
		@ToString
		@NoArgsConstructor
		@AllArgsConstructor
		public static class ResourceRep{
			ItemRep item;
			int quantite;
		}

		@Getter
		@Setter
		@JsonIgnoreProperties(ignoreUnknown = true)
		@ToString
		@NoArgsConstructor
		@AllArgsConstructor
		public static class StatValue{
			String min;
			String max;
			String type;
			public int getMin(){
				if(this.min==null){
					return 0;
				}
				else return Integer.valueOf(min);
			}
			public int getMax(){
				if(this.max==null){
					return 0;
				}
				else return Integer.valueOf(max);
			}
		}




	}

}

