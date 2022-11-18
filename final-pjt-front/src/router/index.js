import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import DetailView from '@/views/DetailView'
import ChoiceView from '@/views/ChoiceView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import ProfileView from '@/views/ProfileView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/choice',
    name: 'choice',
    component: ChoiceView
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  }, 
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  }, 
  {
    path: '/:movie_id',
    name: 'detail',
    component: DetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
