import {
  generateAlgoElements,
  colorSelectedIndex,
  validateForm,
} from './domHandle.js';

const arr = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
const searchedColor = '#00BBD1';
const indexedColor = '#007DFF';

function binarySearch(array, value) {
  let first = 0;
  let last = array.length - 1;
  let mid = null;
  let result = false;

  // Slowing down the algorithm to be visible to others.
  (function loop() {
    // eslint-disable-next-line consistent-return
    setTimeout(() => {
      if (mid !== null) {
        colorSelectedIndex(mid, searchedColor);
      }
      if (first <= last && result !== true) {
        mid = Math.trunc((first + last) / 2);
        colorSelectedIndex(mid, indexedColor);

        if (array[mid] === value) {
          colorSelectedIndex(mid, indexedColor);
          result = true;
          return result;
        } else if (value < array[mid]) {
          colorSelectedIndex(mid, indexedColor);
          last = mid - 1;
        } else {
          colorSelectedIndex(mid, indexedColor);
          first = mid + 1;
        }
      } else {
        colorSelectedIndex(mid, searchedColor);
        result = false;
        return result;
      }

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
    binarySearch(arr, number);
  }
});

