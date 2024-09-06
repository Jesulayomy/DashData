import Image from 'next/image';
import Charts from './components/Charts';
import Header from './components/Header';

export default function Home() {
  return (
    <div className='p-8 px-2 sm:p-10 md:p-16'>
      <Header />
      <main className='flex min-h-screen felx-col items-center justify-center px-4 md:px-8 xl:px-10 py-10 sm:py-32 xl:py-44'>
        <div className='grid xl:grid-cols-3 lg:grid-cols-2 w-full gap-10 max-w-[1400px]'>
          <Charts />
        </div>
      </main>
      <footer className='row-start-3 flex gap-6 flex-wrap items-center justify-center'>
        <div
          className='badge-base LI-profile-badge'
          data-locale='en_US'
          data-size='medium'
          data-theme='dark'
          data-type='VERTICAL'
          data-vanity='jesulayomi'
          data-version='v1'
        >
          <a
            className='badge-base__link LI-simple-link'
            href='https://www.linkedin.com/in/jesulayomi?trk=profile-badge'
          >
            ~ Jesulayomi
          </a>
        </div>
        <a
          className='flex items-center gap-2 hover:underline hover:underline-offset-4 text-center'
          href='https://www.jesulayomi.tech'
          target='_blank'
          rel='noopener noreferrer'
        >
          <Image
            aria-hidden
            src='https://nextjs.org/icons/globe.svg'
            alt='Globe icon'
            width={16}
            height={16}
          />
          Go to jesulayomi.tech →
        </a>
      </footer>
    </div>
  );
}
