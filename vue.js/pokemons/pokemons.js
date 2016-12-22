/*
 * pokemons.js
 * Copyright (C) 2016 tockards <tockards@tockards-ska>
 *
 * Distributed under terms of the MIT license.
 */
var pokeURL = 'http://pokeapi.co/api/v2/pokemon'

/**
 * Actual demo
 */

var demo = new Vue({

  el: '#demo',

  data: {
      pokemons: null,
      pokemon: null,
      branches: ['master', 'dev'],
      currentBranch: 'master'
  },

  created: function () {
    this.fetchData()
  },

  methods: {
    fetchData: function () {
      var xhr = new XMLHttpRequest()
      var self = this
      xhr.open('GET', pokeURL)
      xhr.onload = function () {
        self.pokemons = JSON.parse(xhr.responseText)
      }
      xhr.send()
    },

    doThis: function(pokemonURL){
      var xhr = new XMLHttpRequest()
      var self = this
      xhr.open('GET', pokemonURL)
      this.currentBranch = pokemonURL
      xhr.onload = function () {
        self.pokemon = JSON.parse(xhr.responseText)
      }
      xhr.send()
    }
  }
})

