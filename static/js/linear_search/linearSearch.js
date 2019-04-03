import {
  generateAlgoElements,
  colorSelectedIndex,
  validateForm,
} from './domHandle.js';

const arr = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
const searchedColor = '#00BBD1';
const indexedColor = '#007DFF';


/**
 * Loops through the array to find the value.  When doing so it colors the
 * text on the HTML page that corresponds to the element in the array.
 *
 * @param {*} array
 * @param {number} value
 */
function linearSearch(array, value) {
  let length = array.length;
  let index = 0;

  // Slowing down the algorithm to be visible to others.
  (function loop() {
    // eslint-disable-next-line consistent-return
    setTimeout(() => {
        if (index !== length){
            colorSelectedIndex(index, indexedColor);
            if(array[index] === value){
                return true;
            }
        }else{
            return false;
        }
        colorSelectedIndex(index, searchedColor);
        index += 1;
      loop();
    }, 1000);
  })();
}

// =====================The actual code to run===========================
generateAlgoElements(arr);
const searchButton = document.getElementById('search-button');
searchButton.addEventListener('click', () => {
  const number = validateForm('integer-form');
  if (number !== null) {
    linearSearch(arr, number);
  }
});

