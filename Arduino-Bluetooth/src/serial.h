void toRaspi(){
    if(Serial.available() > 0){
        String command = Serial.readString();
        Serial.println(command);
        if (command == "Send Data"){
            read_all();
        }
    }
}