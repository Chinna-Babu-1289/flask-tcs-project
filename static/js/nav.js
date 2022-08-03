// const links = document.querySelectorAll('.nav-link');

// // if (links.length) {
// // 	links.forEach((link) => {
// // 		link.addEventListener('click', (e) => {
// // 			e.preventDefault();
// // 			links.forEach((link) => {
// // 				link.classList.remove('active');
// // 			});

// // 			link.classList.add('active');
// // 		});
// // 	});
// // }

// if (links.length) {
// 	links.forEach((link) => {
// 		link.onClick(() => {
// 			link.classList.add('active');
// 		});
// 	});
// }


const currentLocation = location.href;
const menuItem = document.querySelectorAll('a')


for(let i =0;i<menuItem.length;i++) {
    if(menuItem[i].href === currentLocation){
        menuItem[i].className = 'active';
    }else{
        menuItem[i].className = '';
    }
}



