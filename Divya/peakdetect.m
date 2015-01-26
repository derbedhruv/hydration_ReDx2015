p = [1 1 1.1 1 0.9 1 1 1.1 1 0.9 1 1.1 1 1 0.9 1 1 1.1 1 1,...
    1 1 1.1 0.9 1 1.1 1 1 0.9 1 1.1 1 1 1.1 1 0.8 0.9 1 1.2 0.9 1,...
    1 1.1 1.2 1 1.5 1 3 2 5 3 2 1 1 1 0.9 1,...
    1 3 2.6 4 3 3.2 2 1 1 0.8 4 4 2 2.5 1 1 1];

% SPECS
lag = 30;
diff = 3.5;
% SPECS

outputmean  = tsmovavg(p,'s',lag,2);
outputstdev = movingstd(p,lag,'backward');

newMean  = zeros(1, length(outputmean));
newStdev = zeros(1, length(outputmean));
signals  = zeros(1, length(outputmean));

newMean(lag-1)  = outputmean(lag);
newStdev(lag-1) = outputstdev(lag);

for i=lag:length(outputmean)
   if (p(i) > newMean(i-1)+diff*newStdev(i-1))
      newMean(i) = newMean(i-1);
      newStdev(i) = newStdev(i-1);
      signals(i) = 0.3;
   else
      newMean(i) = ( newMean(i-1)+p(i) ) / 2 ;
      newStdev(i) = ( newStdev(i-1) + sqrt((p(i) - newMean(i-1))^2) ) / 2; 
      signals(i) = 0;
   end

end

figure;
hold all;
plot(p, ':r', 'LineWidth', 1, 'Color', 'black');
plot(signals, 'LineWidth', 2, 'Color', 'blue');
plot(newMean, 'LineWidth', 2, 'Color', 'red');
plot(newMean+newStdev, 'LineWidth', 2, 'Color', 'green');
