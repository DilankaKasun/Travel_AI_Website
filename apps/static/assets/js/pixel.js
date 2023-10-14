// chat.js

document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('#message-form');
    var input = document.querySelector('#message-input');
    var chatMessages = document.querySelector('#chat-messages');

    // Function to add a message to the chat window
    function addMessage(sender, message) {
        var messageDiv = document.createElement('div');
        messageDiv.textContent = sender + ': ' + message;
        chatMessages.appendChild(messageDiv);
    }

    // Function to send a message to the server via AJAX
    function sendMessageToServer(message, url) {
        $.ajax({
            type: 'POST',
            url: url,
            data: { 'message': message },
            success: function (response) {
                if (response.status === 'success') {
                    // Message sent to the server
                    var userMessages = response.user_messages;
                    var aiMessages = response.ai_messages;
                    updateChatWindow(userMessages, aiMessages);
                }
            }
        });
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        var message = input.value;
        input.value = '';
        addMessage('You', message);
        
        // Determine which URL to use based on sender
        var url = '/send_user_message'; // For user messages
        if (message.startsWith('AI: ')) {
            url = '/send_ai_message'; // For AI messages
        }

        sendMessageToServer(message, url);
    });

    // Function to update the chat window
    function updateChatWindow(userMessages, aiMessages) {
        chatMessages.innerHTML = '';  // Clear the chat window
        for (var i = 0; i < Math.max(Object.keys(userMessages).length, Object.keys(aiMessages).length); i++) {
            if (userMessages[i]) {
                addMessage('User', userMessages[i]);
            }
            if (aiMessages[i]) {
                addMessage('AI', aiMessages[i]);
            }
        }
    }

    // Fetch chat messages from the server and update the chat window
    function fetchMessagesFromServer() {
        $.ajax({
            type: 'GET',
            url: '/get_messages',
            success: function (response) {
                var userMessages = response.user_messages;
                var aiMessages = response.ai_messages;
                updateChatWindow(userMessages, aiMessages);
            }
        });
    }

    fetchMessagesFromServer();
});



"use strict";
const d = document;
d.addEventListener("DOMContentLoaded", function(event) {

    // options
    const breakpoints = {
        sm: 540,
        md: 720,
        lg: 960,
        xl: 1140
    };
    
    var preloader = d.querySelector('.preloader');
    if(preloader) {

        const animations = ['oneByOne', 'delayed', 'sync', 'scenario'];

        new Vivus('loader-logo', {duration: 80, type: 'oneByOne'}, function () {});

        setTimeout(function() {
            preloader.classList.add('show');
        }, 1500);
    }

    if (d.querySelector('.headroom')) {
        var headroom = new Headroom(document.querySelector("#navbar-main"), {
            offset: 0,
            tolerance: {
                up: 0,
                down: 0
            },
        });
        headroom.init();
    }

    // dropdowns to show on hover when desktop
    if (d.body.clientWidth > breakpoints.lg) {
        var dropdownElementList = [].slice.call(document.querySelectorAll('.navbar .dropdown-toggle'))
        dropdownElementList.map(function (dropdownToggleEl) {
            var dropdown = new bootstrap.Dropdown(dropdownToggleEl);
            var dropdownMenu = d.querySelector('.dropdown-menu[aria-labelledby="' + dropdownToggleEl.getAttribute('id') + '"]');

            dropdownToggleEl.addEventListener('mouseover', function () {
                dropdown.show();
            });
            dropdownToggleEl.addEventListener('mouseout', function () {
                dropdown.hide();
            });

            dropdownMenu.addEventListener('mouseover', function () {
                dropdown.show();
            });

            dropdownMenu.addEventListener('mouseout', function () {
                dropdown.hide();
            });
            
        });
    }

    [].slice.call(d.querySelectorAll('[data-background]')).map(function(el) {
        el.style.background = 'url(' + el.getAttribute('data-background') + ')';
    });

    [].slice.call(d.querySelectorAll('[data-background-color]')).map(function(el) {
        el.style.background = 'url(' + el.getAttribute('data-background-color') + ')';
    });

    [].slice.call(d.querySelectorAll('[data-color]')).map(function(el) {
        el.style.color = 'url(' + el.getAttribute('data-color') + ')';
    });

    // Tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    // Popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
      return new bootstrap.Popover(popoverTriggerEl)
    })

    // Datepicker
    var datepickers = [].slice.call(document.querySelectorAll('[data-datepicker]'))
    var datepickersList = datepickers.map(function (el) {
        return new Datepicker(el, {
            buttonClass: 'btn'
          });
    })

    // Toasts
    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl)
    })

    var scroll = new SmoothScroll('a[href*="#"]', {
        speed: 500,
        speedAsDuration: true
    });

    if (d.querySelector('.current-year')) {
        d.querySelector('.current-year').textContent = new Date().getFullYear();
    }

});


const Annually = document.querySelector('#Annually')
const monthly = document.querySelector('#monthly')
function viewPaymetAnnually() {
    Annually.style.display = "none"
    monthly.style.display = "flex"

}
function viewPaymetmonthly() {
    monthly.style.display = "none"
    Annually.style.display = "flex"

}





























