/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var path;

var updateImageUrl = function updateImageUrl() {
  $('#loading').css('display', 'block');

  $.ajax({
    type: "GET",
    url: "/api/get_face_url",
    dataType: 'json',
    async: true,
    success: function success(data) {
      $('#loading').css('display', 'none');
      path = data.path;
      $('#mm').attr("src", "/mm_images/" + data.path);
      $('#mm_face').attr("src", "/mm_images/face-" + data.path);
      var picHeight = $("#mm").height();
      $('.right-div').height(picHeight);
    },
    error: function error() {
      alert("error");
      $('#loading').css('display', 'none');
    }
  });
};

var handleFace = function handleFace(opt) {
  $('#loading').css('display', 'block');
  $.ajax({
    type: "GET",
    url: "/api/handle_face",
    dataType: 'json',
    data: { path: path, opt: opt },
    async: true,
    success: function success(data) {
      console.log(data);
      $('#loading').css('display', 'none');
      updateImageUrl();
    },
    error: function error() {
      alert("error");
      $('#loading').css('display', 'none');
    }
  });
};

$(document).ready(function () {
  updateImageUrl();

  $("#like_btn").click(function () {
    handleFace("like");
  });

  $("#dislike_btn").click(function () {
    handleFace("dislike");
  });

  $("#ignore_btn").click(function () {
    handleFace("ignore");
  });
});

/***/ })
/******/ ]);