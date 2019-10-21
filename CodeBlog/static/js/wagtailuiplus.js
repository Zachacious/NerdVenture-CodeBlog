// Event handler for choice blocks with conditional visibility
function onChoiceHandlerChange(target) {
  const choiceHandler = target.closest('.wagtailuiplus__choice-handler');
  if (choiceHandler !== null) {
    const choiceHandlerValue = choiceHandler.querySelector('select').value;

    let searchContainer;
    // If the chocie handler is a char field, search in the entire tab
    if (choiceHandler.classList.contains('typed_choice_field')) {
      searchContainer = choiceHandler.closest('section');
    // Otherwise, if the choice handler is a choices block, search in the entire struct block
    } else {
       searchContainer = choiceHandler.closest('ul.fields');
    }

    const choiceHandlerIdRegex = /wagtailuiplus__choice-handler--([a-zA-Z\-\_]+)/;
    const choiceHandlerId = choiceHandlerIdRegex.exec(choiceHandler.className)[1];
    const choiceHandlerTargets = searchContainer.querySelectorAll('.wagtailuiplus__choice-handler-target--' + choiceHandlerId);
    const hiddenIfRegex = /wagtailuiplus__choice-handler-hidden-if--([a-zA-Z\-\_]+)/g;
    let hiddenIfValue;
    let matches;
    let hiddenIfs;
    let hiddenIfIndex;
    for (let j = 0; j < choiceHandlerTargets.length; j++) {
      matches = hiddenIfRegex.exec(choiceHandlerTargets[j].className);
      while (matches !== null) {
        hiddenIfValue = matches[1];
        choiceHandlerTargetContainer = choiceHandlerTargets[j].closest('li');
        if (choiceHandlerValue === hiddenIfValue) {
          if (choiceHandlerTargetContainer.hasAttribute('data-wagtailuiplus-hidden-ifs')) {
            hiddenIfs = choiceHandlerTargetContainer.getAttribute('data-wagtailuiplus-hidden-ifs').split(',');
            hiddenIfs.push(hiddenIfValue);
            choiceHandlerTargetContainer.setAttribute('data-wagtailuiplus-hidden-ifs', hiddenIfs.join(','));
          } else {
            choiceHandlerTargetContainer.setAttribute('data-wagtailuiplus-hidden-ifs', hiddenIfValue);
          }
          if (!choiceHandlerTargetContainer.classList.contains('wagtailuiplus__choice-handler-target--hidden')) {
            choiceHandlerTargetContainer.classList.add('wagtailuiplus__choice-handler-target--hidden');
          }
        } else if (choiceHandlerTargetContainer.hasAttribute('data-wagtailuiplus-hidden-ifs')) {
          hiddenIfs = choiceHandlerTargetContainer.getAttribute('data-wagtailuiplus-hidden-ifs').split(',');
          hiddenIfIndex = hiddenIfs.indexOf(hiddenIfValue);
          if (hiddenIfIndex > -1) {
            hiddenIfs.splice(hiddenIfIndex, 1);
            if (hiddenIfs.length === 0) {
              choiceHandlerTargetContainer.classList.remove('wagtailuiplus__choice-handler-target--hidden');
              choiceHandlerTargetContainer.removeAttribute('data-wagtailuiplus-hidden-ifs');
            } else {
              choiceHandlerTargetContainer.setAttribute('data-wagtailuiplus-hidden-ifs', hiddenIfs.join(','));
            }
          }
        }
        matches = hiddenIfRegex.exec(choiceHandlerTargets[j].className);
      }
    }
  }
}

// Event handler for checkboxes with interactivity
function onCheckboxHandlerChange(checkboxHandler) {
  const isChecked = checkboxHandler.checked;
  searchContainer = checkboxHandler.closest('section');
  const checkboxHandlerIdRegex = /wagtailuiplus__checkbox-handler--([a-zA-Z\-\_]+)/;
  const checkboxHandlerId = checkboxHandlerIdRegex.exec(checkboxHandler.closest('.wagtailuiplus__checkbox-handler').className)[1];
  const checkboxHandlerTargets = searchContainer.querySelectorAll('.wagtailuiplus__checkbox-handler-target--' + checkboxHandlerId + '.wagtailuiplus__checkbox-handler-checked-if--checked input[type=checkbox]');
  if (isChecked) {
    for (let i = 0; i < checkboxHandlerTargets.length; i++) {
      if (!checkboxHandlerTargets[i].checked) {
        checkboxHandlerTargets[i].checked = true;
      }
    }
  }
}

// Event handler for checkboxes with interactivity - Reverse dependency
function onCheckboxHandlerTargetChange(checkboxHandlerTarget) {
  const isChecked = checkboxHandlerTarget.checked;
  if (isChecked) {
    return;
  }
  searchContainer = checkboxHandlerTarget.closest('section');
  const checkboxHandlerTargetIdRegex = /wagtailuiplus__checkbox-handler-target--([a-zA-Z\-\_]+)/;
  const checkboxHandlerTargetId = checkboxHandlerTargetIdRegex.exec(checkboxHandlerTarget.closest('li').className)[1];
  const checkboxHandler = searchContainer.querySelector('.wagtailuiplus__checkbox-handler--' + checkboxHandlerTargetId + ' input[type=checkbox]');
  checkboxHandler.checked = false;
}


// Initialize a collapsible panel
function initCollapsablePanel(panelHeader) {
  panelHeader.addEventListener('click', function() {
    if (this.parentElement.classList.contains('wagtailuiplus__panel--collapsed')) {
      this.parentElement.classList.remove('wagtailuiplus__panel--collapsed');
    } else {
      this.parentElement.classList.add('wagtailuiplus__panel--collapsed');
    }
  });
}

// Initialize a collapsable struct block
function initCollapsableStructBlock(structBlockContainer) {
  structBlockContainer.addEventListener('click', function(event) {
    const sequenceControls = event.target.closest('.sequence-controls');
    if (sequenceControls === null) {
      return;
    }
    if (this.id !== event.target.closest('.sequence').id) {
      return;
    }

    if (sequenceControls.parentElement.classList.contains('wagtailuiplus__struct-block--collapsed')) {
      sequenceControls.parentElement.classList.remove('wagtailuiplus__struct-block--collapsed');
    } else {
      sequenceControls.parentElement.classList.add('wagtailuiplus__struct-block--collapsed');
    }
  });
}

// Initialize a smart struct block header
function initSmartStructBlockHeader(structBlockContainer) {
  structBlockContainer.addEventListener('change', function(event) {
    onSmartStructBlockHeaderChange(event);
  });
  structBlockContainer.addEventListener('keyup', function(event) {
    onSmartStructBlockHeaderChange(event);
  });

  let fields;
  let headerLabel;
  const structBlocks = structBlockContainer.children;
  for (i = 0; i < structBlocks.length; i++) {
    if (!structBlocks[i].classList.contains('sequence-member')) {
      continue;
    }
    fields = structBlocks[i].querySelectorAll('.field');
    if (fields.length === 0) {
      continue;
    }
    headerLabel = structBlocks[i].querySelector('.sequence-controls > h3 > label');
    headerLabel.dataset.originalText = headerLabel.innerText;
    // If the first block in the struct block is a char block
    if (fields[0].classList.contains('char_field')) {
      // Set the initial collapsed state and set the header smart title based on the char block value
      structBlocks[i].classList.add('wagtailuiplus__struct-block--collapsed');
      headerLabel.innerText = headerLabel.dataset.originalText + ' - ' + fields[0].querySelector('input[type=text]').value;
    }
  }
}

// Event handler for a smart struct block header change
function onSmartStructBlockHeaderChange(event) {
  const field = event.target.closest('li');
  if (event.target.tagName !== 'INPUT' || field === null || field.previousElementSibling !== null) {
    return;
  }
  const headerLabel = field.closest('.sequence-member').querySelector('.sequence-controls > h3 > label');
  if (headerLabel === null) {
    return;
  }
  if (!headerLabel.hasAttribute('data-original-text')) {
    headerLabel.dataset.originalText = headerLabel.innerText;
  }
  headerLabel.innerText = headerLabel.dataset.originalText + ' - ' + event.target.value;
}


// Initialize a choice handler
function initChoiceHandler(structBlockContainer) {
  structBlockContainer.addEventListener('change', function(event) {
    onChoiceHandlerChange(event.target);
  });
}

// Initialize the struct block watcher
function initStructBlockWatcher(structBlockContainer) {
  const observer = new MutationObserver(onNewStructBlock);
  observer.observe(structBlockContainer, {
    attributes: false,
    childList: true,
    subtree: false,
  });
}

// Event handler for when a new struct block is created
function onNewStructBlock(mutations, observer) {
    let k;
    let l;
    let choiceHandlerSelects;
    for (let j = 0; j < mutations.length; j++) {
      for (k = 0; k < mutations[j].addedNodes.length; k++) {
        // Make sure the choice handler is run for each new choice block
        choiceHandlerSelects = mutations[j].addedNodes[k].querySelectorAll('.wagtailuiplus__choice-handler select');
        for (l = 0; l < choiceHandlerSelects.length; l++) {
          onChoiceHandlerChange(choiceHandlerSelects[l]);
        }
      }
    }
}

// Initialize a checkbox handler
function initCheckboxHandler(checkboxHandlerInput) {
  checkboxHandlerInput.addEventListener('change', function(event) {
    onCheckboxHandlerChange(event.target);
  });
}

// Initialize a checkbox handler target
function initCheckboxHandlerTarget(checkboxHandlerTargetInput) {
  checkboxHandlerTargetInput.addEventListener('change', function(event) {
    onCheckboxHandlerTargetChange(event.target);
  });
}

// Initialize all event handlers on page load
document.addEventListener('DOMContentLoaded', function() {

  // Initialize collapsable panels
  let i;
  const panelHeaders = document.querySelectorAll('.object > .title-wrapper');
  for (i = 0; i < panelHeaders.length; i++) {
    initCollapsablePanel(panelHeaders[i]);
  }

  // Initialize stream field related features
  let observer;
  const structBlockContainers = document.querySelectorAll('.sequence-container.sequence-type-stream > .sequence-container-inner > .sequence');
  for (i = 0; i < structBlockContainers.length; i++) {
    initCollapsableStructBlock(structBlockContainers[i]);
    initSmartStructBlockHeader(structBlockContainers[i]);
    initChoiceHandler(structBlockContainers[i]);
    initStructBlockWatcher(structBlockContainers[i]);
  }

  // Set the initial state of choice handlers contained in stream fields
  const choiceHandlerSelects = document.querySelectorAll('.sequence-container.sequence-type-stream > .sequence-container-inner > .sequence .wagtailuiplus__choice-handler select');
  for (i = 0; i < choiceHandlerSelects.length; i++) {
    onChoiceHandlerChange(choiceHandlerSelects[i]);
  }

  // Initialize choice handlers not contained in stream fields
  const choiceHandlersCharFieldSelects = document.querySelectorAll('li.wagtailuiplus__choice-handler select');
  for (i = 0; i < choiceHandlersCharFieldSelects.length; i++) {
    initChoiceHandler(choiceHandlersCharFieldSelects[i]);
    onChoiceHandlerChange(choiceHandlersCharFieldSelects[i]);
  }

  // Initialize checkbox handlers
  const checkboxHandlerInputs = document.querySelectorAll('li.wagtailuiplus__checkbox-handler input[type=checkbox]');
  for (i = 0; i < checkboxHandlerInputs.length; i++) {
    initCheckboxHandler(checkboxHandlerInputs[i]);
    onCheckboxHandlerChange(checkboxHandlerInputs[i]);
  }

  // Initialize checkbox handler targets
  const checkboxHandlerTargetInputs = document.querySelectorAll('li[class^="wagtailuiplus__checkbox-handler-target--"] input[type=checkbox], li[class*=" wagtailuiplus__checkbox-handler-target--"] input[type=checkbox]');
  for (i = 0; i < checkboxHandlerTargetInputs.length; i++) {
    initCheckboxHandlerTarget(checkboxHandlerTargetInputs[i]);
    onCheckboxHandlerTargetChange(checkboxHandlerTargetInputs[i]);
  }
});
