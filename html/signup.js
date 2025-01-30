function check_email(){
    let input = document.getElementById("email");
    let email_input = input.value;
    // check if email box is left blank.
    if (email_input === ""){
        alert("Please enter an email!");
        return 0;
    }
    let count_at = 0;
    let count_period = 0;
    // get the domain part of the email
    const email_split = email_input.split("@");
    let second_half = email_split[1];

    for (let i = 0; i < email_input.length; i++){
        if (email_input[i] === "@"){
            count_at++;
        }
    }

    for (let j = 0; j < second_half.length; j++){
        if (second_half[j] === "."){
            count_period++;
        }
    }

    if (count_at > 1 || email_input[email_input.length-1] === "@" || email_input[0] === "@" || count_period < 1){
        alert("Invalid email!");
    }
}

function check_age(){
    let input = document.getElementById("bday");
    // birthday input in ms
    let bday_input = input.valueAsNumber;
    // check if user hasnt entered a birthday
    if (Number.isNaN(bday_input)){
        alert("Please enter a birthday!");
        return 0;
    }
    // time since birthday in days
    let time_since_bday = ((((Date.now() - bday_input) / 1000) / 60) / 60) / 24;
    // 13 years ago in days
    let minimum_bday = 4749.25;
    if (time_since_bday < minimum_bday){
        alert("User must be 13 years or older!");
    }
}

function check_nameandpass(){
    let input = document.getElementById("name");
    let input1 = document.getElementById("password")
    if (input.value === ""){
        alert("Please enter a name!");
    }
    if(input1.value === ""){
        alert("Please enter a password!");
    }
}