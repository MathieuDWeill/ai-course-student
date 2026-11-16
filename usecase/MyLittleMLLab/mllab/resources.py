"""Mesures explicites ; pas d'estimation inventée du quota ou de la mémoire GPU."""
import os,threading,time
import psutil
class ResourceMonitor:
    def __enter__(self):
        self.process=psutil.Process(os.getpid());self.start_rss=self.process.memory_info().rss;self.peak_rss=self.start_rss;self.start=time.perf_counter();self.stop=threading.Event()
        def sample():
            while not self.stop.wait(.02):self.peak_rss=max(self.peak_rss,self.process.memory_info().rss)
        self.thread=threading.Thread(target=sample,daemon=True);self.thread.start();return self
    def __exit__(self,*args):
        self.peak_rss=max(self.peak_rss,self.process.memory_info().rss);self.stop.set();self.thread.join();self.elapsed=time.perf_counter()-self.start
    def result(self):
        return {'wall_seconds':self.elapsed,'rss_at_start_bytes':self.start_rss,'sampled_peak_rss_bytes':self.peak_rss,'sampling_seconds':.02,'scope':'Processus Python entier pendant fit+prédiction ; ne mesure pas les allocations natives entre deux échantillons ni la mémoire GPU.'}
