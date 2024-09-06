'use client';

export default function Grid({
  title,
  children
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className='flex flex-col items-center justify-center p-4 border border-slate-500 bg-slate-800/50 rounded-xl h-[400px]'>
      <h3 className='text-2xl font-semibold text-white mb-2'>{title}</h3>
      <div>{children}</div>
    </div>
  );
}
