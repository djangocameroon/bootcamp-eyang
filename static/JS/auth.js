function validateInput(){
    let inputField = document.getElementById("inputField");
    let inputValue = inputField.value.trim();
    const errorMessage = document.getElementById("errorMessage");
    
    if(inputValue ===""){
        inputField.classList.add("shake");
        errorMessage.style.visibility = "visible";

        setTimeout(function(){
        inputField.classList.remove("shake");
        errorMessage.style.visibility = "hidden";
        },500);
    }
    else{ 
      alert("Valid Inputs");
    } 


}