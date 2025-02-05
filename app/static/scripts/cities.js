var state_arr = new Array("Ariana", "Beja", "Ben Arous", "Bizerte", "Gabes", "Gafsa", "Jendouba", "Kairouan", "Kasserine", "Kebili", "Kef", "Mahdia", "Manouba", "Medenine", "Monastir", "Nabeul", "Sfax", "Sidi Bouzid", "Siliana", "Sousse", "Tataouine", "Tozeur", "Tunis", "Zaghouan");

var s_a = new Array();
s_a[0]="";
s_a[1]=" Ariana Ville | Ettadhamen | Kalaat el-Andalous | Mnihla | Raoued | Sidi Thabet | Soukra";
s_a[2]=" Amdoun | Beja Nord | Beja Sud | Goubellat | Medjez el-Bab | Nefza | Teboursouk | Testour";
s_a[3]=" Ben Arous | Boumhel | El Mourouj | Ezzahra | Fouchana | Hammam Chott | Hammam Lif | M'Hamdia | Medjez el-Bab | Mohamedia | Radès";
s_a[4]=" Bizerte Nord | Bizerte Sud | El Alia | Ghar El Melh | Ghezala | Joumine | Mateur | Menzel Bourguiba | Menzel Jemil | Ras Jebel | Sejenane | Tinja | Utique | Zarzouna";
s_a[5]=" Gabes Medina | Gabes Ouest | Gabes Sud | Ghannouch | Hamma | Matmata | Menzel Habib | Metouia | Nouvelle Matmata";
s_a[6]=" Belkhir | El Guettar | Gafsa Nord | Gafsa Sud | Mdhilla | Metlaoui | Moulares | Redeyef | Sidi Aich | Sned";
s_a[7]=" Ain Draham | Balta Bou Aouane | Beni M'Tir | Bou Salem | Fernana | Ghardimaou | Jendouba | Jendouba Nord | Oued Meliz | Tabarka";
s_a[8]=" Bou Hajla | Chebika | Chrarda | Haffouz | Hajeb El Ayoun | Kairouan Nord | Kairouan Sud | Nasrallah | Oueslatia | Sbikha";
s_a[9]=" Ayoun | Ezzouhour | Foussana | Feriana | Hassi El Ferid | Jedelienne | Kasserine Nord | Kasserine Sud | Majel Bel Abbes | Sbeitla | Sbiba | Thala";
s_a[10]=" Douz Nord | Douz Sud | Faouar | Kebili Nord | Kebili Sud | Souk El Ahed";
s_a[11]=" Dahmani | Kalaat Senan | Kalaat Khasba | Kef Est | Kef Ouest | Nebeur | Sakiet Sidi Youssef | Tajerouine";
s_a[12]=" Bou Merdes | Chorbane | Chebba | El Jem | Hbira | Ksour Essef | Mahdia | Melloulech | Ouled Chamekh | Sidi Alouane | Souassi";
s_a[13]=" Borj El Amri | Douar Hicher | El Batan | Jedaida | Manouba | Mornaguia | Oued Ellil | Tebourba";
s_a[14]=" Ben Gardane | Beni Khedache | Djerba - Ajim | Djerba - Houmt Souk | Djerba - Midoun | Medenine Nord | Medenine Sud | Sidi Makhlouf | Zarzis";
s_a[15]=" Bekalta | Bembla | Beni Hassen | Jammel | Ksar Hellal | Ksibet el-Mediouni | Moknine | Monastir | Ouerdanine | Sahline | Sayada-Lamta-Bou Hajar | Teboulba | Zeramdine";
s_a[16]=" Beni Khalled | Beni Khiar | Bou Argoub | Dar Chaabane El Fehri | El Haouaria | El Mida | Grombalia | Hammam Ghezaz | Hammamet | Kelibia | Korba | Menzel Bouzelfa | Menzel Temime | Nabeul | Soliman | Takelsa";
s_a[17]=" Agareb | Bir Ali Ben Khalifa | El Amra | El Hencha | Graiba | Jebiniana | Kerkennah | Mahres | Menzel Chaker | Sakiet Eddaier | Sakiet Ezzit | Sfax Ouest | Sfax Sud | Sfax Ville | Skhira";
s_a[18]=" Bir El Hafey | Cebbala Ouled Asker | Jelma | Mazzouna | Meknassy | Menzel Bouzaiane | Ouled Haffouz | Regueb | Sidi Ali Ben Aoun | Sidi Bouzid Est | Sidi Bouzid Ouest | Souk Jedid";
s_a[19]=" Bargou | Bou Arada | El Aroussa | El Krib | Gaafour | Kesra | Makthar | Rouhia | Siliana Nord | Siliana Sud";
s_a[20]=" Akouda | Bouficha | Enfidha | Hammam Sousse | Hergla | Kalâa Kebira | Kalâa Seghira | Kondar | Msaken | Sidi Bou Ali | Sidi El Hani | Sousse Jawhara | Sousse Medina | Sousse Riadh | Sousse Sidi Abdelhamid";
s_a[21]=" Bir Lahmar | Dehiba | Ghomrassen | Remada | Smar | Tataouine Nord | Tataouine Sud";
s_a[22]=" Degache | Hazoua | Nefta | Tameghza | Tozeur";
s_a[23]=" Bab Bhar | Bab Souika | Bardo | Carthage | Cité El Khadra | Djebel Jelloud | El Kabaria | El Menzah | El Omrane | El Omrane supérieur | El Ouardia | Ettahrir | Ezzouhour | Hrairia | La Goulette | La Marsa | Le Kram | Médina | Séjoumi | Sidi El Béchir | Sidi Hassine";
s_a[24]=" Bir Mcherga | El Fahs | Nadhour | Saouaf | Zaghouan | Zriba";

function print_state(state_id){
	var option_str = document.getElementById(state_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select State','');
	option_str.selectedIndex = 0;
	for (var i=0; i<state_arr.length; i++) {
		option_str.options[option_str.length] = new Option(state_arr[i],state_arr[i]);
	}
}

function print_city(city_id, city_index){
    var option_str = document.getElementById(city_id);
    option_str.length=0;
    option_str.options[0] = new Option('Select City','');
    option_str.selectedIndex = 0;
    var city_arr = s_a[city_index].split("|");
    for (var i=0; i<city_arr.length; i++) {
        option_str.options[option_str.length] = new Option(city_arr[i],city_arr[i]);
    }
}