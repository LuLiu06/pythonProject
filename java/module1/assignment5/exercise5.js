
const year=parseInt(prompt("Enter a year to check if it's a leap year;  "))

function isLeapYear(year){
  if(year%4===0){
    if(year%100===0){
      return year%400===0;
    }
    return true;
  }
  return false;
}

const outputDiv=document.getElementById("output");

if(!isNaN(year)){
  if (isLeapYear(year)){
    outputDiv.textContent=`${year} is a leap year.`;

  }else {
    outputDiv.textContent = `${year} is not a leap year`;
  }

}else{
  outputDiv.textContent="Invalid input.Please refresh the page and enter a valid year.";
}