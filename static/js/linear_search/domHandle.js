const algoText = document.getElementById('algo-text');

/**
 * Generate the list of elements in the array on to the HTML page.
 *
 * @export
 * @param {*} array
 */
export function generateAlgoElements(array) {
  let span = null;

  // eslint-disable-next-line no-unused-vars
  array.forEach((value, index) => {
    span = document.createElement('span');
    span.innerText = ` ${value} `;
    span.style.color = 'red';
    span.className = 'algo-num';
    algoText.appendChild(span);
  });
}

/**
 * Delete all elements that are a part of the algorithm text block.
 *
 * @export
 */
export function deleteAlgoChildren() {
  while (algoText.firstChild) {
    algoText.removeChild(algoText.lastChild);
  }
}


/**
 * Color the looked at element for the algorithm. The index given is always one
 * less than the correct element.  The first element in the childNodes is text.
 *
 * @export
 * @param {number} index
 */
export function colorSelectedIndex(index, color = 'blue') {
  const idx = index + 1;
  const children = algoText.childNodes;
  const child = children[idx];
  child.style.color = 'white';
  child.style.backgroundColor = color;
}


/**
 * Validates the number given by the user is between 0-21 exclusively and makes
 * sure it is a number to begin with.
 *
 * @export
 * @param {String} formName
 * @returns
 */
export function validateForm(formName) {
  let number = document.forms[formName].integer.value;
  if (!number.isNaN) {
    number = Math.trunc(number);
    document.forms[formName].integer = number;
  } else {
    const text = document.getElementById('error-text');
    text.innerText = `${number} is not a number.`;
    return null;
  }
  if (number < 21 && number > 0) {
    return number;
  } else {
    const text = document.getElementById('error-text');
    text.innerText = `${number} is not a number between 0 and 21.`;
    return null;
  }
}
