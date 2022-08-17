const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

//Event handlers functions
// ? Show Error Function
const showError = (input, message) => {
    const formControl = input.parentElement;
    console.log(formControl);
    formControl.className = 'form-control error';
    const small = formControl.querySelector('small');
    small.innerHTML = message;
    // console.log(formControl);
};

// ? Show Error Function
const showSuccess = (input, message) => {
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
    // console.log(formControl);
};

// ? Email Validator Function
const checkEmail = (input) => {
    // js-email-validator regex: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    const re = /^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$/;
    if (re.test(input.value.trim())) {
        showSuccess(input);
    } else {
        showError(input, 'Email is not valid');
    }
};

//  check Required fields
const checkRequired = (inputArr) => {
    inputArr.forEach((input) => {
        if (input.value.trim() === '') {
            showError(input, `${getFieldName(input)} is Required`);
        } else {
            showSuccess(input);
        }
    });
};

const checkLength = (input, min, max) => {
    if (input.value.length < min) {
        showError(
            input,
            `${getFieldName(input)} must be atleast ${min} characters`
        );
    } else if (input.value.length > max) {
        showError(
            input,
            `${getFieldName(input)} must be less than ${max} characters`
        );
    } else {
        showSuccess(input);
    }
};

const checkPasswordMatch = (input1, input2) => {
    // console.log(input1.value, input2.value);
    if (input1.value !== input2.value) {
        showError(input2, 'Passwords do not match');
    }
};

const passwordValidate = (input) => {
    pattern = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    if (!pattern.test(input)) {
        showError(
            input,
            'Password should contain one uppercase , lowercase and @,$,&,%!'
        );
    }
};

const getFieldName = (input) => {
    return input.id.charAt(0).toUpperCase() + input.id.slice(1);
};

// Event Listeners
form.addEventListener('submit', (e) => {
    e.preventDefault();

    checkRequired([ username, email, password, password2 ]);
    checkLength(username, 3, 15); //[fieldName, minlength, maxlength]
    checkLength(password, 6, 25);
    checkLength(password2, 6, 25);
    checkEmail(email);
    checkPasswordMatch(password, password2);
    // passwordValidate(password);
});

// form.addEventListener('submit', (e) => {
// 	e.preventDefault();
// 	if (username.value === '') {
// 		showError(username, 'Username is Required');
// 	} else {
// 		showSuccess(username);
// 	}
// 	if (email.value === '') {
// 		showError(email, 'Email is Required');
// 	} else if (!isValidEmail(email.value)) {
// 		showError(email, 'Email is not Valid');
// 	} else {
// 		showSuccess(email);
// 	}
// 	if (password.value === '') {
// 		showError(password, 'Password is Required');
// 	} else {
// 		showSuccess(password);
// 	}
// 	if (password2.value === '') {
// 		showError(password2, 'Password is Required');
// 	} else {
// 		showSuccess(password2);
// 	}
// });
