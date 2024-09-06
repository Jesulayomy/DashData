"use client";

import { api } from '../utils/api';


export default function Header() {
  const randomAPI = () => {
    api.get('/randomize/');
  };
  return (
    <header className='text-center'>
      <h1 className='text-4xl font-bold text-center md:text-5xl'>
        DashBoard Charts for BlockHouse
      </h1>
      <p className='text-center text-md md:text-lg p-2'>
        ~ By Jesulayomi (Layomi), for the Full Stack Developer Intern position
        at blockhouse
      </p>
      <button
        className='border p-2 rounded-xl hover:bg-zinc-700 border-slate-500/50'
        onClick={() => randomAPI()}
      >
        Rebuild database
      </button>
    </header>
  );
}
